"""schemas.py"""

from typing import List, Literal, Optional, Tuple
from pydantic import BaseModel, Field
from core.schemas.companies import CompanyReference, ResolvedCompany


class StrategyExecutionResult(BaseModel):
    candidates: List[Tuple[ResolvedCompany, float]] = Field(default_factory=list)
    """List of (company, confidence_score) tuples found by this strategy"""

    was_skipped: bool = False
    """Whether the strategy was skipped (e.g., missing required context)"""

    execution_time_ms: Optional[int] = None
    """Time taken to execute this strategy"""

    @property
    def has_results(self) -> bool:
        return len(self.candidates) > 0

    @property
    def best_match(self) -> Optional[Tuple[ResolvedCompany, float]]:
        """Get the highest confidence match from this strategy"""
        if not self.candidates:
            return None
        return max(self.candidates, key=lambda x: x[1])

    def add_candidate(self, company: ResolvedCompany, confidence: float) -> None:
        """Add a candidate to the results"""
        self.candidates.append((company, confidence))


class AlternativeCompanyMatch(BaseModel):
    """An alternative match to a company that was found, but not the best match."""

    company: ResolvedCompany
    """The company that was found."""
    confidence_score: float = Field(..., ge=0, le=1)
    """How close this is to the best match. 1 being the same confidence level as the best match."""
    is_perfect_overlap: bool = False
    """Whether this match is a perfect overlap with the best match - i.e. they have the same confidence score - NOT the same company."""

    def to_string(self) -> str:
        """Convert the alternative match to a string."""
        return f"{self.company.name} ({self.company.domain}) -- Score: {self.confidence_score}"


ResolutionMethod = Literal[
    "uuid",
    "exact_domain",
    "exact_name",
    "case_insensitive_name",
    "inames",
    "fuzzy_name",
    "contextual",
    "multi_field_search",
    "failed",
]
"""How the company was resolved.

    1. Exact UUID match (highest confidence)
    2. Exact domain match (highest confidence)
    3. Exact name match - Looks at 'name' field, not 'alt_names' or 'legal_names'
    4. Case-insensitive name match - Looks at 'name' field, not 'alt_names' or 'legal_names'
    5. inames - Case insensitive look at 'name', 'legal_names', and 'alt_names'
    6. Fuzzy name search
    7. Contextual resolution
    8. Multi-field search - Look at fields beyond just the name and domain
"""


# NOTE: We might want to have non-zero confidence scores for 'failed' resolution methods.
# For example, if an utterance definitely does NOT have a company reference, we should return
# a high confidence score.
class CompanyResolutionResult(BaseModel):
    """The result of resolving a company reference."""

    resolved_company: Optional[ResolvedCompany] = None
    """The company that was resolved from the reference."""

    confidence_score: float = Field(..., ge=0, le=1)
    """Confidence in the resolution (0-1). 1 is the highest confidence (exact match)."""

    input_reference: CompanyReference
    """The input reference that was used to find the resolved company."""

    resolution_method: ResolutionMethod
    """How the company was resolved."""

    alternative_matches: List[AlternativeCompanyMatch] = Field(default_factory=list)
    """Alternative matches that were found, but not the best match."""

    used_context: bool = False
    """Whether contextual resolution was used."""

    methods_tried: List[ResolutionMethod] = Field(default_factory=list)
    """The resolution methods that were tried."""

    resolution_duration_ms: int = 0
    """The time taken to resolve the reference, in milliseconds."""

    @property
    def is_resolved(self) -> bool:
        """Did we find a company or not?"""
        return self.resolution_method != "failed"

    @property
    def is_ambiguous(self) -> bool:
        """Whether the 'best match' isn't clear based on all of the matching methods tried."""
        if len(self.alternative_matches) == 0:
            return False
        if self.confidence_score >= 0.97:
            return False
        # If we're here, see the gap between the best and the next best.
        gap = self.confidence_score - self.alternative_matches[0].confidence_score
        return gap < 0.2

    @property
    def is_exact_match(self) -> bool:
        """Whether the resolution is an exact match (either uuid, exact_domain or exact_name) and there are no significant alternative matches.

        We consider a significant alternative match to be one that is not a perfect overlap with the best match.
        """
        significant_alternative_matches = [
            match
            for match in self.alternative_matches
            if match.is_perfect_overlap is False
        ]
        return (
            self.resolution_method in ["exact_domain", "exact_name", "uuid"]
            and len(significant_alternative_matches) == 0
        )

    def to_string(self, short: bool = False) -> str:
        """Convert the resolution result to a string."""
        ambiguous_string = " **Ambiguous**" if self.is_ambiguous else ""
        if short:
            if self.is_resolved:
                return f"'{self.input_reference.value}' -> '{self.resolved_company.name}' ({self.resolved_company.domain}) -- Score: {self.confidence_score}{ambiguous_string}"
            return f"'{self.input_reference.value}' -> '{self.resolution_method}' (Tried: {', '.join(self.methods_tried)}){ambiguous_string}"

        if self.is_resolved:
            return (
                f"Input: '{self.input_reference.value}'\n"
                f"  Resolved: '{self.resolved_company.name}' ({self.resolved_company.domain}){ambiguous_string}\n"
                f"  Confidence: {self.confidence_score}\n"
                f"  Duration: {self.resolution_duration_ms}ms\n"
                f"  Method: {self.resolution_method}\n"
                f"  Used context: {self.used_context}\n"
                f"  Alternative matches: {', '.join([match.to_string() for match in self.alternative_matches])}\n"
                f"  Methods tried: {self.methods_tried}"
            )
        else:
            return (
                f"Input: '{self.input_reference.value}'\n"
                f"  Duration: {self.resolution_duration_ms}ms\n"
                f"  Method: {self.resolution_method}\n"
                f"  Used context: {self.used_context}\n"
                f"  Alternative matches: {', '.join([match.to_string() for match in self.alternative_matches])}\n"
                f"  Methods tried: {self.methods_tried}"
            )


"""service.py"""

"""
Refactored CompanyEntityResolver with cleaner design.

Key improvements:
1. Consistent strategy return types using StrategyExecutionResult
2. Better handling of multiple candidates from search strategies
3. Cleaner separation of concerns
4. No more messy tuples or type unions
"""

import asyncio
import time
import logging
from uuid import UUID
from typing import Optional, List, Callable, Awaitable, Dict, TYPE_CHECKING
from dataclasses import dataclass
from temporalio import activity
from core.logging import configure_logger
from core.schemas.exists import ExistsResponse
from core.schemas.companies import IdentifiedCompany  # noqa E621
from core.schemas.companies import CompanyReference, ResolutionContext
from app.schemas.search import SearchRequest
from app.schemas.companies import (
    SearchResultCompany,
)
from app.services.companies.entity_resolution.schemas import (
    ResolvedCompany,
    ResolutionMethod,
    AlternativeCompanyMatch,
    CompanyResolutionResult,
    StrategyExecutionResult,
)
from app.services.companies.parsers.entity_resolution import CompanyReferenceParser

if TYPE_CHECKING:
    from app.services.companies.storage import CompanyStorageService
    from app.services.companies.search import CompanySearchService


@dataclass
class ResolutionStrategy:
    """Clean strategy definition with consistent interface"""

    name: ResolutionMethod
    base_confidence: float
    max_confidence: float
    func: Callable[
        [
            CompanyReference,
            Optional[ResolutionContext],
            Optional[str],
        ],
        Awaitable[StrategyExecutionResult],
    ]
    requires_context: bool = False


# TODO: Add a caching layer
class CompanyEntityResolver:
    """Resolve a single company reference to a canonical company entity in our database."""

    def __init__(
        self,
        storage_service: "CompanyStorageService",
        search_service: Optional["CompanySearchService"] = None,
        logger: Optional[logging.Logger] = None,
    ):
        self.storage_service = storage_service
        self.search_service = search_service
        self.logger = logger or configure_logger(__name__)

        # Define strategies with clean, consistent interface
        self.strategies = [
            ResolutionStrategy(
                name="uuid",
                base_confidence=1.00,
                max_confidence=1.00,
                func=self._resolve_by_uuid,
            ),
            ResolutionStrategy(
                name="exact_domain",
                base_confidence=1.00,
                max_confidence=1.00,
                func=self._resolve_by_domain,
            ),
            ResolutionStrategy(
                name="exact_name",
                base_confidence=0.97,
                max_confidence=0.97,
                func=self._resolve_by_exact_name,
            ),
            ResolutionStrategy(
                name="inames",
                base_confidence=0.45,
                max_confidence=0.95,
                func=self._resolve_by_inames,
            ),
            # ResolutionStrategy(
            #     name="multi_field_search",
            #     base_confidence=0.6,
            #     max_confidence=0.9,
            #     func=self._resolve_by_multi_field_search,
            # ),
        ]

    @activity.defn
    async def resolve(
        self,
        reference: str | UUID | dict | CompanyReference,
        context: Optional[dict | ResolutionContext] = None,
        return_threshold: float = 0.95,
        min_confidence_score: float = 0.5,
        tenant_db_slug: Optional[str] = None,
    ) -> CompanyResolutionResult:
        """Resolve a single company reference to a canonical company entity in our database.

        Args:
        - reference: The company reference to resolve. Can be:
                - A string: "Google", "google.com", "GOOGL"
                - A dict (fitting the CompanyReference schema): {"name": "Google", "domain": "google.com"}
                - A CompanyReference object
        - context: Optional context to improve resolution accuracy
        - return_threshold: If this is reached, we'll return early. If not, we'll continue trying other methods until we hit the threshold, or run out of methods.
        - min_confidence_score: The minimum confidence score to return a result. Keep this high to avoid running all strategies if we know they won't have a high enough confidence score.
        - tenant_db_slug: The tenant database to use. If not provided, we won't be able to resolve tenant-specific companies.

        Returns:
            CompanyResolutionResult: The resolution result with the best match and alternatives.

        Examples:
        ```python
        # Simple domain resolution
        result = await resolver.resolve("google.com")

        # Name-based resolution with context
        result = await resolver.resolve(
            "Amazon",
            context={
                "field_name": "competitors",
                "source_company": IdentifiableCompany(
                    id=UUID("123e4567-e89b-12d3-a456-426614174000"),
                    domain="shopify.com",
                    name="Shopify",
                )
            }
        )
        ```
        """
        start_time = time.time()

        # 1. Parse inputs
        ref = self._parse_reference(reference)
        ctx = self._parse_context(context)

        # 2. Try resolution strategies in order of speed/accuracy
        all_candidates: List[tuple[ResolvedCompany, float, ResolutionMethod]] = []
        methods_tried: List[ResolutionMethod] = []
        used_context = False

        for strategy in self.strategies:
            # Skip if strategy can't meet minimum threshold
            if strategy.max_confidence < min_confidence_score:
                self.logger.debug(
                    f"Skipping {strategy.name}: max confidence {strategy.max_confidence} "
                    f"< min required {min_confidence_score}"
                )
                continue

            # Check context requirements
            if strategy.requires_context and (not ctx or ctx.is_empty):
                self.logger.debug(f"Skipping {strategy.name}: requires context")
                continue

            # Execute strategy
            result = await strategy.func(ref, ctx, tenant_db_slug)

            if not result.was_skipped:
                methods_tried.append(strategy.name)

            if result.has_results:
                # Track if we used context
                if strategy.requires_context:
                    used_context = True

                # Add all candidates from this strategy
                for company, confidence in result.candidates:
                    all_candidates.append((company, confidence, strategy.name))

                # Early return if we found a high-confidence match
                if result.best_match and result.best_match[1] >= return_threshold:
                    best_company, best_confidence = result.best_match
                    return self._build_resolution_result(
                        resolved_company=best_company,
                        confidence_score=round(best_confidence, 2),
                        method=strategy.name,
                        all_candidates=all_candidates,
                        input_ref=ref,
                        min_confidence=min_confidence_score,
                        used_context=used_context,
                        methods_tried=methods_tried,
                        start_time=start_time,
                    )

        # 3. Process all candidates to find best match and alternatives
        if all_candidates:
            return self._build_resolution_result(
                resolved_company=None,  # Will be determined from candidates
                confidence_score=0,
                method="multi",
                all_candidates=all_candidates,
                input_ref=ref,
                min_confidence=min_confidence_score,
                used_context=used_context,
                methods_tried=methods_tried,
                start_time=start_time,
            )

        # No candidates found
        return self._build_failed_result(
            input_ref=ref,
            methods_tried=methods_tried,
            used_context=used_context,
            start_time=start_time,
        )

    @activity.defn
    async def resolve_many(
        self,
        references: List[str] | List[dict] | List[CompanyReference],
        context: Optional[dict | ResolutionContext] = None,
        deduplicate: bool = True,
        remove_unresolved: bool = True,
        return_threshold: float = 0.95,
        min_confidence_score: float = 0.5,
        tenant_db_slug: Optional[str] = None,
    ) -> List[CompanyResolutionResult]:
        """Resolve multiple company references efficiently.

        Args:
        - references: List of company references to resolve. Can be:
                - A list of strings: ["Google", "google.com", "GOOGL"]
                - A list of dicts (fitting the CompanyReference schema): [{"name": "Google", "domain": "google.com"}]
                - A list of CompanyReference objects
        - context: Optional context to improve resolution accuracy
        - deduplicate: If True, avoid returning the same company multiple times
        - remove_unresolved: If True, remove results that are not resolved
        - return_threshold: If this is reached, we'll return early. If not, we'll continue trying other methods until we hit the threshold, or run out of methods.
        - min_confidence_score: The minimum confidence score to return a result. Keep this high to avoid running all strategies if we know they won't have a high enough confidence score.
        - tenant_db_slug: The tenant database to use. If not provided, we won't be able to resolve tenant-specific companies.

        Examples:
        ```python
        # Resolve a list of competitor names
        result = await resolver.resolve_many(
            ["Google", "Amazon", "MSFT"],
            context={"field_name": "competitors"}
        )
        ```
        """
        # 1. Parse inputs
        refs = [self._parse_reference(ref) for ref in references]
        ctx = self._parse_context(context)

        # 2. Run the resolution strategies.
        # For now, just run the single-reference resolver in parallel.
        # TODO: Optimize this for batch queries, etc.
        results = await asyncio.gather(
            *[
                self.resolve(
                    ref,
                    ctx,
                    return_threshold,
                    min_confidence_score,
                    tenant_db_slug=tenant_db_slug,
                )
                for ref in refs
            ]
        )

        # 3. Remove unresolved results.
        if remove_unresolved:
            results = [result for result in results if result.is_resolved]

        # 4. Deduplicate results
        if deduplicate:
            results = self._deduplicate_results(results)

        return results

    # Strategy implementations - now all return StrategyExecutionResult

    async def _resolve_by_uuid(
        self,
        ref: CompanyReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """UUID resolution - cleanest possible"""
        result = StrategyExecutionResult()

        if not ref.id:
            result.was_skipped = True
            return result

        exists = await self.storage_service.check_company_exists_by_id(
            ref.id, include_unverified=True, tenant_context=tenant_db_slug
        )

        if company := await self._resolved_company_from_exists(exists, tenant_db_slug):
            result.add_candidate(company, 1.0)

        return result

    async def _resolve_by_domain(
        self,
        ref: CompanyReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """Domain resolution"""
        result = StrategyExecutionResult()

        if not ref.domain:
            result.was_skipped = True
            return result

        exists = await self.storage_service.check_company_exists_by_domain(
            ref.domain, include_unverified=True, tenant_context=tenant_db_slug
        )

        if company := await self._resolved_company_from_exists(exists, tenant_db_slug):
            result.add_candidate(company, 1.0)

        return result

    async def _resolve_by_exact_name(
        self,
        ref: CompanyReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """Exact name resolution"""
        result = StrategyExecutionResult()

        if not ref.name:
            result.was_skipped = True
            return result

        exists = await self.storage_service.check_company_exists_by_name(
            ref.name,
            match_type="exact",
            include_unverified=True,
            tenant_context=tenant_db_slug,
        )

        if company := await self._resolved_company_from_exists(exists, tenant_db_slug):
            result.add_candidate(company, 0.97)

        return result

    async def _resolve_by_inames(
        self,
        ref: CompanyReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """Resolution via inames search - handles multiple results"""
        result = StrategyExecutionResult()

        if not ref.name or not self.search_service:
            result.was_skipped = True
            return result

        search_response = await self.search_service.search(
            SearchRequest(query=ref.name, type="name", include_additional_fields=True),
            tenant_db_slug=tenant_db_slug,
        )

        # Convert search results to candidates
        for search_result in search_response.results:
            if company := await self._resolved_company_from_search_result(
                search_result, tenant_db_slug
            ):
                # Use the relevance score from search, bounded by strategy's confidence range
                confidence = self._scale_confidence(
                    search_result.relevance_score,
                    self.strategies[3].base_confidence,  # inames strategy
                    self.strategies[3].max_confidence,
                )
                result.add_candidate(company, confidence)

        return result

    async def _resolve_by_multi_field_search(
        self,
        ref: CompanyReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """Multi-field search - handles multiple results"""
        result = StrategyExecutionResult()

        if not self.search_service or (not ref.name and not ref.domain):
            result.was_skipped = True
            return result

        # Try domain first, then name
        query = ref.domain or ref.name
        search_response = await self.search_service.search(
            query, tenant_db_slug=tenant_db_slug
        )

        # Convert all search results
        for search_result in search_response.results:
            if company := await self._resolved_company_from_search_result(
                search_result, tenant_db_slug
            ):
                # confidence = self._scale_confidence(
                #     search_result.relevance_score, 0.4, 0.9
                # )
                result.add_candidate(company, search_result.relevance_score)

        return result

    # Helper methods

    def _scale_confidence(
        self, raw_score: float, min_conf: float, max_conf: float
    ) -> float:
        """Scale a 0-1 score to a confidence range"""
        return min_conf + (raw_score * (max_conf - min_conf))

    async def _resolved_company_from_search_result(
        self, search_result: SearchResultCompany, tenant_db_slug: Optional[str]
    ) -> Optional[ResolvedCompany]:
        """Convert a search result to a ResolvedCompany"""
        # Create an ExistsResponse from the search result
        exists = ExistsResponse(
            in_shared=search_result.in_shared,
            in_tenant=search_result.in_tenant,
            shared_id=search_result.id if search_result.in_shared else None,
            tenant_id=search_result.tenant_id,
        )

        company = await self.storage_service.get_company_by_exists_response(
            exists, tenant_context=tenant_db_slug, prefer_tenant=False
        )

        if not company:
            return None

        return ResolvedCompany(
            id=company.id,
            domain=company.domain,
            name=company.name,
            alt_names=company.alt_names or [],
            alt_domains=company.alt_domains or [],
            source_location=company.storage_location,
            source_slug=(
                tenant_db_slug if company.storage_location != "shared" else None
            ),
            tenant_id=search_result.tenant_id,
        )

    async def _resolved_company_from_exists(
        self, exists_response: ExistsResponse, tenant_db_slug: Optional[str]
    ) -> Optional[ResolvedCompany]:
        """Convert exists response to resolved company (existing logic)"""
        if not exists_response.exists or exists_response.has_multiple_matches:
            return None

        company = await self.storage_service.get_company_by_exists_response(
            exists_response, tenant_context=tenant_db_slug, prefer_tenant=False
        )

        return ResolvedCompany(
            id=company.id,
            domain=company.domain,
            name=company.name,
            alt_names=company.alt_names or [],
            alt_domains=company.alt_domains or [],
            source_location=company.storage_location,
            source_slug=(
                tenant_db_slug if company.storage_location != "shared" else None
            ),
            tenant_id=exists_response.tenant_id,
        )

    def _build_resolution_result(
        self,
        resolved_company: Optional[ResolvedCompany],
        confidence_score: float,
        method: ResolutionMethod,
        all_candidates: List[tuple[ResolvedCompany, float, ResolutionMethod]],
        input_ref: CompanyReference,
        min_confidence: float,
        used_context: bool,
        methods_tried: List[ResolutionMethod],
        start_time: float,
    ) -> CompanyResolutionResult:
        """Build result with proper handling of alternatives"""

        duration_ms = int((time.time() - start_time) * 1000)

        # If we have candidates, process them
        if all_candidates:
            # Group by company (using domain as key)
            company_groups: Dict[
                str, List[tuple[ResolvedCompany, float, ResolutionMethod]]
            ] = {}

            for company, conf, method in all_candidates:
                key = company.domain
                if key not in company_groups:
                    company_groups[key] = []
                company_groups[key].append((company, conf, method))

            # Find best match for each company
            best_matches = []
            for domain, matches in company_groups.items():
                # Get highest confidence match for this company
                best = max(matches, key=lambda x: x[1])
                best_matches.append(best)

            # Sort all matches by confidence
            best_matches.sort(key=lambda x: x[1], reverse=True)

            if best_matches:
                # Top match
                best_company, best_conf, best_method = best_matches[0]

                # Only return if meets minimum threshold
                if best_conf >= min_confidence:
                    # Build alternatives
                    alternatives = []
                    for company, conf, _ in best_matches[1:]:
                        alternatives.append(
                            AlternativeCompanyMatch(
                                company=company,
                                confidence_score=(
                                    round(conf / best_conf if best_conf > 0 else 0, 2)
                                ),
                                is_perfect_overlap=abs(conf - best_conf) < 0.001,
                            )
                        )

                    return CompanyResolutionResult(
                        resolved_company=best_company,
                        confidence_score=round(best_conf, 2),
                        resolution_method=best_method,
                        input_reference=input_ref,
                        alternative_matches=alternatives,
                        used_context=used_context,
                        methods_tried=methods_tried,
                        resolution_duration_ms=duration_ms,
                    )

        # No match or below threshold
        return self._build_failed_result(
            input_ref, methods_tried, used_context, start_time
        )

    def _build_failed_result(
        self,
        input_ref: CompanyReference,
        methods_tried: List[ResolutionMethod],
        used_context: bool,
        start_time: float,
    ) -> CompanyResolutionResult:
        """Build a failed resolution result"""
        duration_ms = int((time.time() - start_time) * 1000)

        return CompanyResolutionResult(
            resolved_company=None,
            confidence_score=0.0,
            resolution_method="failed",
            input_reference=input_ref,
            alternative_matches=[],
            used_context=used_context,
            methods_tried=methods_tried,
            resolution_duration_ms=duration_ms,
        )

    def _parse_reference(self, reference) -> CompanyReference:
        return CompanyReferenceParser.parse_reference(reference)

    def _parse_context(self, context) -> Optional[ResolutionContext]:
        try:
            return CompanyReferenceParser.parse_context(context)
        except Exception:
            return None

    def _deduplicate_results(
        self, results: List[CompanyResolutionResult]
    ) -> List[CompanyResolutionResult]:
        """Remove duplicate companies from results, keeping the highest confidence match."""
        deduplicated_ids = set()
        deduplicated = []
        for result in results:
            if result.is_resolved:
                if result.resolved_company.domain not in deduplicated_ids:
                    deduplicated_ids.add(result.resolved_company.domain)
                    deduplicated.append(result)
            else:
                # Still return empty results.
                deduplicated.append(result)
        return deduplicated


# MARK: - Tests


async def test_resolve():
    import uuid  # noqa: F401
    from core.db import DatabaseManager
    from app.services.companies.storage import CompanyStorageService
    from app.services.companies.search import CompanySearchService

    db = DatabaseManager()
    db.initialize(
        write_url="postgresql://dev:password@localhost:5432/doro_db",
        read_url="postgresql://reader:read0nlyPass@localhost:5432/doro_db",
    )
    resolver = CompanyEntityResolver(
        storage_service=CompanyStorageService(db),
        search_service=CompanySearchService(db),
    )
    tests = [
        # uuid.UUID("7b105410-afe3-4d72-a208-50528db3c2e8"),
        # "google.com",
        # "domain:google.com ",
        "GM",
        # "GOOGL",
        # "name:Amazon",
        # "amazon",
        # "amzon",
        # "amazon.com",
        "twitter.com",
        # IdentifiedCompany(id=uuid.uuid4(), domain="google.com", name="Google"),
        # {"id": uuid.uuid4(), "domain": "apple.com", "name": "Apple"},
        # "Airlines",
    ]
    results = await resolver.resolve_many(
        tests, min_confidence_score=0.65, deduplicate=False, remove_unresolved=False
    )
    for result in results:
        print(result.to_string(short=False))


if __name__ == "__main__":
    asyncio.run(test_resolve())

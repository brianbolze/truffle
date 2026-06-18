"""schemas.py"""

from typing import List, Literal, Optional, Tuple
from pydantic import BaseModel, Field
from core.schemas.products import Product, ProductReference


class StrategyExecutionResult(BaseModel):
    candidates: List[Tuple[Product, float]] = Field(default_factory=list)
    """List of (product, confidence_score) tuples found by this strategy"""

    was_skipped: bool = False
    """Whether the strategy was skipped (e.g., missing required context)"""

    execution_time_ms: Optional[int] = None
    """Time taken to execute this strategy"""

    @property
    def has_results(self) -> bool:
        return len(self.candidates) > 0

    @property
    def best_match(self) -> Optional[Tuple[Product, float]]:
        """Get the highest confidence match from this strategy"""
        if not self.candidates:
            return None
        return max(self.candidates, key=lambda x: x[1])

    def add_candidate(self, product: Product, confidence: float) -> None:
        """Add a candidate to the results"""
        self.candidates.append((product, confidence))


class AlternativeMatch(BaseModel):
    """An alternative match to a reference that was found, but not the best match."""

    product: Product
    """The product that was found."""
    confidence_score: float = Field(..., ge=0, le=1)
    """How close this is to the best match. 1 being the same confidence level as the best match."""
    is_perfect_overlap: bool = False
    """Whether this match is a perfect overlap with the best match - i.e. they have the same confidence score - NOT the same product."""

    def to_string(self) -> str:
        """Convert the alternative match to a string."""
        return f"{self.product.product_name} ({self.product.company_domain}) -- Score: {self.confidence_score}"


ResolutionMethod = Literal[
    "uuid",  # Exact ID
    "name_and_company_domain",  # Direct lookup using product_name and company_domain
    "name",  # Name without company context (only used when unique)
    "multi_field_search",  # Search service fallback
    "failed",
]
"""How the product was resolved.

    1. Exact UUID match (highest confidence)
    2. Multi-field search - Compare string to product name, company name, product alt_names, and more.
"""


class ProductResolutionResult(BaseModel):
    """The result of resolving a product reference."""

    resolved_product: Optional[Product] = None
    """The product that was resolved."""

    confidence_score: float = Field(..., ge=0, le=1)
    """Confidence in the resolution (0-1). 1 is the highest confidence (exact match)."""

    input_reference: ProductReference
    """The input reference that was used to find the resolved product."""

    resolution_method: ResolutionMethod
    """How the product was resolved."""

    alternative_matches: List[AlternativeMatch] = Field(default_factory=list)
    """Alternative matches that were found, but not the best match."""

    used_context: bool = False
    """Whether contextual resolution was used."""

    methods_tried: List[ResolutionMethod] = Field(default_factory=list)
    """The resolution methods that were tried."""

    resolution_duration_ms: int = 0
    """The time taken to resolve the reference, in milliseconds."""

    @property
    def is_resolved(self) -> bool:
        """Did we find a product or not?"""
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

    def to_string(self, short: bool = False) -> str:
        """Convert the resolution result to a string."""
        ambiguous_string = " **Ambiguous**" if self.is_ambiguous else ""
        if short:
            if self.is_resolved:
                return f"'{self.input_reference.value}' -> '{self.resolved_product.product_name}' ({self.resolved_product.company_domain}) -- Score: {self.confidence_score}{ambiguous_string}"
            return f"'{self.input_reference.value}' -> '{self.resolution_method}' (Tried: {', '.join(self.methods_tried)}){ambiguous_string}"

        if self.is_resolved:
            return (
                f"Input: '{self.input_reference.value}'\n"
                f"  Resolved: '{self.resolved_product.product_name}' ({self.resolved_product.company_domain}){ambiguous_string}\n"
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

import time
import logging
from core.logging import configure_logger
from uuid import UUID
from typing import Optional, List, Callable, Awaitable, Dict, TYPE_CHECKING
from dataclasses import dataclass
from core.schemas.products import Product, ProductReference, ResolutionContext
from app.services.products.entity_resolution.schemas import (
    ResolutionMethod,
    AlternativeMatch,
    ProductResolutionResult,
    StrategyExecutionResult,
)
from app.services.products.parsers.entity_resolution import ProductReferenceParser
from temporalio import activity

if TYPE_CHECKING:
    from app.services.products.storage.products import ProductStorageService
    from app.services.products.search.service import (
        ProductSearchService,
        SearchResultProduct,
    )
    from app.services.companies.entity_resolution.service import CompanyEntityResolver


@dataclass
class ResolutionStrategy:
    name: ResolutionMethod
    base_confidence: float
    max_confidence: float
    func: Callable[
        [
            ProductReference,
            Optional[ResolutionContext],
            Optional[str],
        ],
        Awaitable[StrategyExecutionResult],
    ]
    requires_context: bool = False


class ProductEntityResolver:
    """Resolve a single product reference to a canonical product entity in our database."""

    def __init__(
        self,
        storage_service: "ProductStorageService",
        search_service: Optional["ProductSearchService"] = None,
        company_resolver: Optional["CompanyEntityResolver"] = None,
        logger: Optional[logging.Logger] = None,
    ):
        self.storage_service = storage_service
        self.search_service = search_service
        self.company_resolver = company_resolver
        self.logger = logger or configure_logger(__name__)

        self.strategies = [
            ResolutionStrategy(
                name="uuid",
                base_confidence=1.00,
                max_confidence=1.00,
                func=self._resolve_by_uuid,
            ),
            ResolutionStrategy(
                name="name_and_company_domain",
                base_confidence=0.95,
                max_confidence=0.98,
                func=self._resolve_by_name_and_company_domain,
            ),
            ResolutionStrategy(
                name="name",
                base_confidence=0.80,
                max_confidence=0.90,
                func=self._resolve_by_name_only,
            ),
            ResolutionStrategy(
                name="multi_field_search",
                base_confidence=0.9,
                max_confidence=1.00,
                func=self._resolve_by_search,
            ),
        ]

    @activity.defn
    async def resolve_product(
        self,
        reference: str | UUID | dict | ProductReference,
        context: Optional[dict | ResolutionContext] = None,
        return_threshold: float = 0.95,
        min_confidence_score: float = 0.5,
        tenant_db_slug: Optional[str] = None,
    ) -> ProductResolutionResult:
        """Resolve a single product reference to a canonical product entity in our database."""
        start_time = time.time()

        # 1. Parse inputs
        ref = self._parse_reference(reference)
        ctx = self._parse_context(context)
        ref = await self._adjust_value_for_provided_company(ref, tenant_db_slug)

        # 2. Try resolution strategies in order of speed/accuracy
        all_candidates: List[tuple[Product, float, ResolutionMethod]] = []
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
                for product, confidence in result.candidates:
                    all_candidates.append((product, confidence, strategy.name))

                # Early return if we found a high-confidence match
                if result.best_match and result.best_match[1] >= return_threshold:
                    best_product, best_confidence = result.best_match
                    return self._build_resolution_result(
                        resolved_product=best_product,
                        confidence_score=best_confidence,
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
                resolved_product=None,  # Will be determined from candidates
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

    # Strategy implementations - now all return StrategyExecutionResult
    # TODO: Add more strategies to handle other types of references
    # Ex. "iPhone | Apple" -> { "name": "iPhone", "company_name": "Apple" }
    # Ex. "iPhone (apple.com)" -> { "name": "iPhone", "company_domain": "apple.com" }

    async def _resolve_by_uuid(
        self,
        ref: ProductReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """UUID resolution - cleanest possible"""
        result = StrategyExecutionResult()

        if not ref.product_id:
            result.was_skipped = True
            return result

        candidate = await self.storage_service.get_product_by_id(
            ref.product_id, tenant_db_slug=tenant_db_slug
        )
        if candidate:
            result.add_candidate(candidate, 1.0)

        return result

    async def _resolve_by_search(
        self,
        ref: ProductReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """Multi-field search - use search service to find best match"""
        result = StrategyExecutionResult()
        if not self.search_service:
            result.was_skipped = True
            return result
        search_response = await self.search_service.search_products(
            {
                "query": ref.value,
                "type": "auto",
                "include_additional_fields": True,
                "limit": 5,
            },
            tenant_db_slug=tenant_db_slug,
        )
        # Convert search results to candidates
        for search_result in search_response.results:
            if product := await self._resolved_product_from_search_result(
                search_result, tenant_db_slug
            ):
                result.add_candidate(product, search_result.relevance_score)

        return result

    # ------------------------------------------------------------------
    # New storage-based strategy: product_name + company_domain
    # ------------------------------------------------------------------

    async def _resolve_by_name_and_company_domain(
        self,
        ref: ProductReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """Exact name lookup scoped by company domain.

        This is a high-confidence match when both fields are provided. It leverages
        the storage service (fast DB query) and avoids the heavier search stack.
        """
        result = StrategyExecutionResult()

        # Require both pieces of information.
        if not (ref.product_name and ref.company_domain):
            result.was_skipped = True
            return result

        product = await self.storage_service.get_product_by_name(
            product_name=ref.product_name,
            company_domain=ref.company_domain,
            tenant_db_slug=tenant_db_slug,
        )

        if product:
            # Confidence tweaks: perfect if company also matches by context.
            confidence = 0.95
            # If reference also included company_id and matches, bump a bit.
            if ref.company_id and product.company_id == ref.company_id:
                confidence = 0.97
            result.add_candidate(product, confidence)

        return result

    async def _resolve_by_name_only(
        self,
        ref: ProductReference,
        context: Optional[ResolutionContext],
        tenant_db_slug: Optional[str],
    ) -> StrategyExecutionResult:
        """Attempt to resolve using only product_name when company is unknown.

        We treat this as lower-confidence because the name might not be unique.
        If multiple products share the same name we add them all with same score
        which downstream logic will mark as ambiguous.
        """
        result = StrategyExecutionResult()

        if not ref.product_name:
            result.was_skipped = True
            return result

        try:
            product = await self.storage_service.get_product_by_name(
                product_name=ref.product_name,
                company_domain=None,
                company_id=None,
                tenant_db_slug=tenant_db_slug,
            )
            if product:
                result.add_candidate(product, 0.85)
        except Exception:
            pass

        return result

    # Helpers

    def _build_resolution_result(
        self,
        resolved_product: Optional[Product],
        confidence_score: float,
        method: ResolutionMethod,
        all_candidates: List[tuple[Product, float, ResolutionMethod]],
        input_ref: ProductReference,
        min_confidence: float,
        used_context: bool,
        methods_tried: List[ResolutionMethod],
        start_time: float,
    ):
        """Build result with proper handling of alternatives"""

        duration_ms = int((time.time() - start_time) * 1000)

        # If we have candidates, process them
        if all_candidates:
            # Group by product (using company-domain|product-name as key)
            product_groups: Dict[str, List[tuple[Product, float, ResolutionMethod]]] = (
                {}
            )

            for product, conf, method in all_candidates:
                key = f"{product.company_domain}|{product.product_name}"
                if key not in product_groups:
                    product_groups[key] = []
                product_groups[key].append((product, conf, method))

            # Find best match for each product
            best_matches = []
            for key, matches in product_groups.items():
                # Get highest confidence match for this product
                best = max(matches, key=lambda x: x[1])
                best_matches.append(best)
            # Sort all matches by confidence
            best_matches.sort(key=lambda x: x[1], reverse=True)

            if best_matches:
                # Top match
                best_product, best_conf, best_method = best_matches[0]

                # Only return if meets minimum threshold
                if best_conf >= min_confidence:
                    # Build alternatives
                    alternatives = []
                    for product, conf, _ in best_matches[1:]:
                        alternatives.append(
                            AlternativeMatch(
                                product=product,
                                confidence_score=(
                                    round(conf / best_conf if best_conf > 0 else 0, 2)
                                ),
                                is_perfect_overlap=abs(conf - best_conf) < 0.001,
                            )
                        )
                    return ProductResolutionResult(
                        resolved_product=best_product,
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
        input_ref: ProductReference,
        methods_tried: List[ResolutionMethod],
        used_context: bool,
        start_time: float,
    ) -> ProductResolutionResult:
        """Build a failed resolution result"""
        duration_ms = int((time.time() - start_time) * 1000)
        return ProductResolutionResult(
            resolved_product=None,
            confidence_score=0.0,
            resolution_method="failed",
            input_reference=input_ref,
            alternative_matches=[],
            used_context=used_context,
            methods_tried=methods_tried,
            resolution_duration_ms=duration_ms,
        )

    def _parse_reference(self, reference) -> ProductReference:
        return ProductReferenceParser.parse_reference(reference)

    def _parse_context(self, context) -> Optional[ResolutionContext]:
        return ProductReferenceParser.parse_context(context)

    async def _resolved_product_from_search_result(
        self, search_result: "SearchResultProduct", tenant_db_slug: Optional[str]
    ) -> Optional[Product]:
        """Convert a search result to a Product"""
        # Use the storage service to get the product
        return await self.storage_service.get_product_by_id(
            search_result.id, tenant_db_slug=tenant_db_slug
        )

    async def _adjust_value_for_provided_company(
        self, ref: ProductReference, tenant_db_slug: Optional[str]
    ) -> ProductReference:
        """If the company domain or name is provided, append it to the value to query against."""
        if not self.company_resolver:
            return ref
        if not ref.company_domain and not ref.company_name:
            return ref
        if ref.company_name:
            # For now, just append this to the value, as long as it doesn't already start with it
            if not ref.value.startswith(ref.company_name):
                ref.value = f"{ref.company_name} | {ref.value}"
            else:
                return ref
        if ref.company_domain:
            # If the domain is provided, we need to get the company name from the database
            company_resolution = await self.company_resolver.resolve(
                ref.company_domain, tenant_db_slug=tenant_db_slug
            )
            if company := company_resolution.resolved_company:
                if ref.value.startswith(company.name):
                    return ref
                ref.value = f"{company.name} | {ref.value}"
                ref.company_name = company.name
                ref.company_domain = company.domain
                ref.company_id = company.id
            else:
                return ref
        return ref


# Testing


async def test_resolve():
    import uuid  # noqa: F401
    from core.db import DatabaseManager
    from app.services.products.storage.products import ProductStorageService
    from app.services.products.search.service import ProductSearchService

    db = DatabaseManager()
    db.initialize(
        write_url="postgresql://dev:password@localhost:5432/doro_db",
        read_url="postgresql://reader:read0nlyPass@localhost:5432/doro_db",
    )
    resolver = ProductEntityResolver(
        storage_service=ProductStorageService(db),
        search_service=ProductSearchService(db),
    )
    tests = [
        # uuid.UUID("2a26322d-76c2-42e1-974d-8bfde0483c1b"),
        # "iPhone",
        # "iPhone | Apple",
        # "Ford - F-150",
        # "Apple",
        # "F-150",
        # "Super Duty",
        # "Ford Focus",
        # "Ford | Focus",
        "iPhone 16 Pro",
        # {"product_name": "iPhone", "company_name": "Apple"},
        # {"product_name": "iPhone", "company_domain": "apple.com"},
        # {"product_name": "iPhone", "company_name": "Apple"},
        # {"product_name": "iPhone", "company_domain": "apple.com"},
    ]
    for test in tests:
        result = await resolver.resolve_product(test)
        print(result.to_string(short=False))


if __name__ == "__main__":
    import asyncio

    asyncio.run(test_resolve())

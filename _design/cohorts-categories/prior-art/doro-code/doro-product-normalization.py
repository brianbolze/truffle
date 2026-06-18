import logging
from core.logging import configure_logger
from typing import Optional, Tuple, List, Dict, Any
from pydantic import BaseModel
from uuid import UUID
from core.schemas.products import ProductReference
from app.schemas.products import ProductCandidate, ProductCandidateDatapoints
from app.services.products.normalization.base import (
    FieldNormalizationResult,
    ProductFieldNormalizer,
)
from app.services.products.normalization.product_name import ProductNameNormalizer
from app.services.products.normalization.company_domain import CompanyDomainNormalizer
from app.services.products.entity_resolution.service import ProductEntityResolver
from temporalio import activity


MIN_IDENTITY_VALIDATION_SCORE = 50

from uuid import UUID
from enum import Enum
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field, field_serializer
from core.schemas.exists import StorageLocation
from core.schemas.products import StableProductIdentifier
from core.schemas.research.validation import ValidationMetadata
from core.schemas.base import CommonSerializersMixin
from core.schemas.algos.reconciliation import ConfidenceBreakdown
from core.schemas.research.product_datapoints import ProductDatapointFull


ReviewState = Literal["pending", "valid", "invalid", "failed"]
ConfidenceLevel = Literal["high", "medium", "low"]


class ProductCandidate(BaseModel):
    """Candidate product for potential indexing or enrichment."""

    field_values: Dict[str, Any] = Field(default_factory=dict)
    """The potential datapoints for different fields of the candidate product."""
    confidence_scores: Dict[str, float] = Field(default_factory=dict)
    """The confidence scores for each field value."""
    field_normalization_state: Dict[str, ReviewState] = Field(default_factory=dict)
    """The review state of each field value."""
    identity_validation_score: Optional[int] = None
    """Confidence that 'this is a real product' after doing validation. 0-100 value."""
    validation_metadata: ValidationMetadata = Field(default_factory=ValidationMetadata)
    """The validation metadata for the candidate product."""
    deduplicated: bool = False
    """Whether this candidate has been deduplicated against existing products."""
    metadata: Optional[Dict[str, Any]] = None
    """Additional info about discovery, sourcing, processing, etc."""

    @property
    def name(self) -> Optional[str]:
        return (
            self.field_values.get("product_name")
            or self.field_values.get("name")
            or self.field_values.get("colloquial_name")
        )

    @property
    def company_domain(self) -> Optional[str]:
        return self.field_values.get("company_domain") or self.field_values.get(
            "domain"
        )

    @property
    def company_name(self) -> Optional[str]:
        return self.field_values.get("company_name")

    @property
    def parent_product_name(self) -> Optional[str]:
        return (
            self.field_values.get("parent_product_name")
            or self.field_values.get("parent_name")
        )

    @property
    def stable_identifier(self) -> Optional[StableProductIdentifier]:
        if not self.name:
            return None
        if not self.company_domain:
            return None
        return StableProductIdentifier(
            name=self.name,
            company_domain=self.company_domain,
            alt_names=self.field_values.get("alt_names", []),
            parent_product_name=self.parent_product_name,
        )

    @property
    def identifier_normalization_state(self) -> ReviewState:
        """Whether the fields in the identifier have been normalized."""
        if not self.stable_identifier:
            return "pending"

        identifier = self.stable_identifier
        company_domain_state = self.field_normalization_state.get(
            "company_domain", "pending"
        )
        name_state = self.field_normalization_state.get("name", "pending")
        alt_names_state = self.field_normalization_state.get("alt_names", "pending")
        if not identifier.alt_names:
            alt_names_state = "valid"

        states = [company_domain_state, name_state, alt_names_state]
        if not company_domain_state or not name_state:
            return "pending"
        if any(state == "pending" for state in states):
            return "pending"
        elif any(state == "invalid" for state in states):
            # Anything being invalid means the whole thing is invalid!
            return "invalid"

        # Must be valid if we get here.
        return "valid"

    @property
    def ready_to_index(self) -> bool:
        return (
            self.deduplicated
            # and self.identifier_normalization_state == "valid"
            and not self.needs_normalization
            and self.validation_metadata.did_complete
            and self.identity_validation_score is not None
            and self.identity_validation_score > 30
        )

    @property
    def needs_identity_review(self) -> bool:
        return (
            not self.identity_validation_score
            or not self.validation_metadata.did_complete
        )

    @property
    def needs_normalization(self) -> bool:
        if not self.field_normalization_state:
            return True

        for field_name in self.field_values.keys():
            if (
                field_name not in self.field_normalization_state
                or self.field_normalization_state[field_name] == "pending"
            ):
                return True
        return False

    @field_serializer("identity_validation_score")
    def serialize_identity_validation_score(
        self, identity_validation_score: int | None
    ) -> Optional[int]:
        if identity_validation_score is None:
            return None
        return int(identity_validation_score)

    def fail_validation_completely(
        self, signal_name: str, resulting_score: int = 0, timestamp: datetime = None
    ):
        checked_at = timestamp or datetime.now(timezone.utc)
        self.validation_metadata.fail_validation_completely(
            signal_name=signal_name, timestamp=checked_at
        )
        self.identity_validation_score = resulting_score

    def pass_validation(
        self, signals: List[str], timestamp: datetime = None, resulting_score: int = 100
    ):
        checked_at = timestamp or datetime.now(timezone.utc)
        self.validation_metadata.pass_validation(signals=signals, timestamp=checked_at)
        self.identity_validation_score = resulting_score


class ProductCandidateDatapoints(BaseModel):
    """New datapoints / potential changes to apply to a product record. This should always be associated with a specific product ID / stable identifier."""

    field_values: Dict[str, Any] = Field(default_factory=dict)
    """The field values to apply to the product record. E.g. The datapoint values to create."""
    confidence_scores: Dict[str, float] = Field(default_factory=dict)
    """Confidence scores for the new values / datapoints."""
    field_normalization_state: Dict[str, ReviewState] = Field(default_factory=dict)
    """The review state of each field value."""
    metadata: Optional[Dict[str, Any]] = None
    """Additional info about sourcing, extraction, etc."""

    @property
    def name(self) -> Optional[str]:
        return (
            self.field_values.get("product_name")
            or self.field_values.get("name")
            or self.field_values.get("colloquial_name")
        )

    @property
    def company_domain(self) -> Optional[str]:
        return self.field_values.get("company_domain") or self.field_values.get(
            "domain"
        )

    @property
    def company_name(self) -> Optional[str]:
        return self.field_values.get("company_name")

    @property
    def needs_normalization(self) -> bool:
        for field_name in self.field_values.keys():
            if (
                field_name not in self.field_normalization_state
                or self.field_normalization_state[field_name] == "pending"
            ):
                return True
        return False


# Search

class SearchMethod(str, Enum):
    """The method used to search for a product."""

    NAME = "name"
    INAME = "iname"
    NAMES = "names"
    FUZZY_MULTI_FIELD = "fuzzy_multi_field"
    SEMANTIC = "semantic"
    PG_FULL_TEXT = "pg_full_text"
    MULTI = "multi"


class SearchResultProduct(BaseModel):
    """A single search result"""

    id: UUID
    relevance_score: float  # 0.0 to 1.0, how well this matches the query

    source_location: StorageLocation
    source_slug: Optional[str] = None  # Tenant slug if tenant-specific
    tenant_id: Optional[UUID] = None  # If it exists in tenant db

    # Additional fields (if requested)
    product_name: Optional[str] = None
    company_id: Optional[UUID] = None

    @property
    def in_tenant(self) -> bool:
        return self.source_location.in_tenant

    @property
    def in_shared(self) -> bool:
        return self.source_location.in_shared


class SearchResponse(BaseModel):
    """Complete search response"""

    # Results
    results: List[SearchResultProduct]
    total_matches: int  # Total found (might be > len(results) due to limits)

    # Performance
    duration_ms: int

    # Search metadata
    search_method: SearchMethod  # Which strategy was used

    original_query: str
    sanitized_query: Optional[str] = None  # If we cleaned/normalized it

    # Convenience methods
    def as_ids(self) -> List[UUID]:
        """Quick access to just Product IDs, in rank order."""
        return [result.id for result in self.results]

    def get_top_match(self, min_score: float = 0.8) -> Optional[SearchResultProduct]:
        """Get the best match if it meets the threshold"""
        if self.results and self.results[0].relevance_score >= min_score:
            return self.results[0]
        return None

    def filter_by_score(self, min_score: float) -> List[SearchResultProduct]:
        """Get only results above a certain relevance threshold"""
        return [r for r in self.results if r.relevance_score >= min_score]

    def to_string(self) -> str:
        """Return a string representation of the search response"""
        message = f"Query: '{self.original_query}'"
        if self.sanitized_query:
            message += f" (Sanitized: '{self.sanitized_query}')"
        message += f" -> Total Matches: {self.total_matches} - Duration: {self.duration_ms}ms - Method: '{self.search_method.value}'\n"
        for result in self.results[:5]:
            message += f"  {result.product_name} ({result.company_id}) - Score: {result.relevance_score}"
            if result.source_location == StorageLocation.TENANT:
                message += f" (Tenant: {result.source_slug})"
            elif result.source_location == StorageLocation.BOTH:
                message += " (Shared + Tenant)"
            message += "\n"
        if len(self.results) > 5:
            message += f"And {len(self.results) - 5} more results...\n"
        return message


# Additional Schemas

class FieldSources(BaseModel, CommonSerializersMixin):
    confidence: ConfidenceLevel = Field(
        ...,
        description="The confidence level of the chosen value.",
        examples=["high", "medium", "low"],
    )
    """The confidence level of the chosen value."""
    confidence_score: float = Field(
        ...,
        description="A 0-1 confidence score for the chosen value.",
        examples=[0.95, 0.8, 0.5],
    )
    """A 0-1 confidence score for the chosen value."""
    confidence_breakdown: ConfidenceBreakdown
    """Detailed breakdown of confidence score components."""
    used_shared_datapoints: bool
    """Whether the shared datapoints were used while refreshing the field."""
    used_tenant_datapoints: bool
    """Whether the tenant datapoints were used while refreshing the field."""
    supporting_datapoints: List[ProductDatapointFull]
    """The datapoints that were used to support the chosen value."""
    conflicting_datapoints: List[ProductDatapointFull]
    """The datapoints that were used to conflict with the chosen value."""
    last_updated_time: datetime
    "The timestamp of the last update to the field."

    @field_serializer("last_updated_time", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)


class FieldNormalizationResult(BaseModel):
    field_name: str
    """The name of the field that was normalized."""
    input: Any
    """The original value of the field."""
    output: Optional[Any] = None
    """The normalized value of the field, if different from the input."""
    review_state: ReviewState = "pending"
    """The review state of the normalized field value."""
    should_discard: bool = False
    """Whether the field value should be discarded."""
    confidence: float = 1.0
    """The confidence score of the normalized field value."""
    message: str = ""
    """A message explaining the result."""


class ProductFieldNormalizer:
    """A base class for product field normalizers."""

    field_name: str
    """The name of the field that this normalizer is responsible for."""

    def normalize(self, field_value: Any) -> FieldNormalizationResult:
        """Normalize a field value."""
        return FieldNormalizationResult(
            field_name=self.field_name,
            input=field_value,
            output=field_value,
            review_state="valid",
        )



class PotentialDuplicate(BaseModel):
    """A potential duplicate of a product candidate."""

    confidence_score: float
    """The confidence score that this is a duplicate (0-1). 1 is a perfect match."""
    shared_product_id: Optional[UUID] = None
    """The ID of the shared product that is a potential duplicate."""
    tenant_product_id: Optional[UUID] = None
    """The ID of the tenant-specific product that is a potential duplicate."""


class ProductValidationResult(BaseModel):
    candidate: ProductCandidate
    """The updated candidate - with updated confidence score and validation signals fields."""
    message: Optional[str] = None
    """A message explaining the result."""


# TODO: Normalize the field NAMES as well
class ProductNormalizationService:
    """Responsible for normalizing potential field values before they can be stored as datapoints in the database, and also verifying product candidates."""

    def __init__(
        self,
        product_resolver: Optional[ProductEntityResolver] = None,
        logger: Optional[logging.Logger] = None,
    ):
        self.product_resolver = product_resolver
        self.logger = logger or configure_logger(
            __name__, logging.INFO, "[NORMALIZATION]"
        )
        self.normalizers: Dict[str, ProductFieldNormalizer] = {
            "name": ProductNameNormalizer(),
            "company_domain": CompanyDomainNormalizer(),
        }

    @activity.defn
    async def normalize_product_candidate_datapoints(
        self, datapoints: ProductCandidateDatapoints, remove_invalid: bool = True
    ) -> ProductCandidateDatapoints:
        """Normalizes the field values of a product candidate's datapoints."""
        if isinstance(datapoints, dict):
            datapoints = ProductCandidateDatapoints.model_validate(datapoints)

        if not datapoints.needs_normalization:
            self.logger.warning("Candidate datapoints already normalized, skipping.")
            return datapoints

        # Normalize the candidate fields.
        newly_normalized_fields = []
        normalized_fields, invalid_fields, pending_fields = self._build_field_dicts(
            datapoints
        )
        datapoints.field_values = normalized_fields

        # Now, normalize the pending_fields
        if pending_fields:
            self.logger.info(f"Normalizing {len(pending_fields)} fields...")
            try:
                normalization_result = await self.normalize_field_values(pending_fields)
                for field_name, field_result in normalization_result.items():
                    if field_result.review_state == "valid":
                        normalized_fields[field_name] = field_result.output
                        datapoints.field_normalization_state[field_name] = "valid"
                        newly_normalized_fields.append(field_name)
                    elif field_result.review_state == "invalid":
                        invalid_fields[field_name] = field_result.output
                        datapoints.field_normalization_state[field_name] = "invalid"
                        if remove_invalid:
                            self.logger.info(
                                "Field %s is invalid, removing field from datapoints",
                                field_name,
                            )
                            datapoints.field_values.pop(field_name, None)
                            datapoints.confidence_scores.pop(field_name, None)
                            datapoints.field_normalization_state.pop(field_name, None)
                        else:
                            self.logger.info(
                                "Field %s is invalid, keeping field in datapoints",
                                field_name,
                            )
                            datapoints.field_normalization_state[field_name] = "invalid"
                    else:
                        # Assume it's still pending if not valid or invalid
                        self.logger.info(
                            "Could not normalize field %s, marking as failed",
                            field_name,
                        )
                        pending_fields[field_name] = field_result.output
                        datapoints.field_normalization_state[field_name] = "failed"
            except Exception as e:
                self.logger.error(
                    "Error normalizing fields: %s. Marking all pending fields as failed.",
                    str(e),
                )
                for field_name in pending_fields:
                    datapoints.field_normalization_state[field_name] = "failed"
                    pending_fields[field_name] = None

        if not datapoints.needs_normalization:
            self.logger.info("Fields normalized successfully.")
        else:
            self.logger.info(
                "Fields normalized, but some fields are still pending normalization."
            )
        return datapoints

    @activity.defn
    async def normalize_product_candidate_fields(
        self, candidate: ProductCandidate | dict, remove_invalid: bool = True
    ) -> ProductCandidate:
        """Normalizes the field values of a product candidate."""
        if isinstance(candidate, dict):
            candidate = ProductCandidate.model_validate(candidate)

        self.logger.info(
            f"Normalizing candidate fields: {candidate.name} ({candidate.company_domain})"
        )
        self.logger.info(candidate.field_values)

        if not candidate.needs_normalization:
            self.logger.info(
                "Candidate fields already normalized. Skipping normalization step..."
            )
            return candidate

        # Normalize the candidate fields.
        newly_normalized_fields = []
        normalized_fields, invalid_fields, pending_fields = self._build_field_dicts(
            candidate
        )
        candidate.field_values = normalized_fields

        # Now, normalize the pending_fields
        if pending_fields:
            self.logger.info(f"Normalizing {len(pending_fields)} fields...")
            try:
                normalization_result = await self.normalize_field_values(pending_fields)
                for field_name, field_result in normalization_result.items():
                    if field_result.review_state == "valid":
                        normalized_fields[field_name] = field_result.output
                        candidate.field_values[field_name] = field_result.output
                        candidate.field_normalization_state[field_name] = "valid"
                        newly_normalized_fields.append(field_name)
                    elif field_result.review_state == "invalid":
                        invalid_fields[field_name] = field_result.output
                        candidate.field_normalization_state[field_name] = "invalid"
                        if remove_invalid:
                            self.logger.info(
                                "Field %s is invalid, removing field from candidate",
                                field_name,
                            )
                            candidate.field_values.pop(field_name, None)
                            candidate.confidence_scores.pop(field_name, None)
                            candidate.field_normalization_state.pop(field_name, None)
                    else:
                        # Assume it's still pending if not valid or invalid
                        self.logger.info(
                            "Could not normalize field %s, marking as failed",
                            field_name,
                        )
                        pending_fields[field_name] = field_result.output
                        candidate.field_normalization_state[field_name] = "failed"

            except Exception as e:
                self.logger.error(
                    "Error normalizing fields: %s. Marking all pending fields as failed.",
                    str(e),
                )
                for field_name in pending_fields:
                    candidate.field_normalization_state[field_name] = "failed"
                    pending_fields[field_name] = None

        # TODO: Check if name or company_domain changed after normalization and reset identity validation if needed
        if not candidate.needs_normalization:
            self.logger.info("Fields normalized successfully.")
        else:
            self.logger.info(
                "Fields normalized, but some fields are still pending normalization."
            )
        return candidate

    @activity.defn
    async def normalize_and_verify_product_candidate(
        self, candidate: ProductCandidate, remove_invalid: bool = True
    ) -> Tuple[ProductCandidate, Optional[List[PotentialDuplicate]]]:
        """Normalizes and validates / invalidates a product candidate."""
        # Normalize the candidate fields first
        candidate = await self.normalize_product_candidate_fields(
            candidate, remove_invalid
        )
        if candidate.needs_normalization:
            self.logger.info(
                "Fields normalized, but some fields are still pending normalization. Skipping verification..."
            )
            return candidate, None

        self.logger.info("Continuing with identity verification...")
        validation_result = await self.validate_product_candidate(candidate)
        candidate = validation_result.candidate
        if validation_result.message:
            self.logger.info(validation_result.message)
        if (
            not candidate.identity_validation_score
            or candidate.identity_validation_score < MIN_IDENTITY_VALIDATION_SCORE
        ):
            self.logger.warning(
                "Identity validation failed. Skipping de-duplication..."
            )
            return candidate, None

        if not candidate.deduplicated:
            self.logger.info("Checking for potential duplicates...")
            potential_duplicates = await self.check_product_duplicates(candidate)
            if not potential_duplicates:
                self.logger.info("No duplicates found.")
                candidate.deduplicated = True
            else:
                self.logger.warning(
                    "Verification failed. Potential duplicates found: %s",
                    potential_duplicates,
                )
                candidate.deduplicated = False

        if candidate.ready_to_index:
            self.logger.info(
                "Candidate passed normalization and identity verification. Ready to index."
            )

        return candidate, potential_duplicates

    @activity.defn
    async def validate_product_candidate(
        self, candidate: ProductCandidate | dict
    ) -> ProductValidationResult:
        """Runs validators and updates the candidate's confidence score and validation signals."""
        if isinstance(candidate, dict):
            candidate = ProductCandidate.model_validate(candidate)

        def fail_validation(message: str, signal_name: str):
            candidate.fail_validation_completely(
                signal_name=signal_name, resulting_score=0
            )
            return ProductValidationResult(candidate=candidate, message=message)

        # Check if it has the minimum required fields
        if not candidate.name:
            return fail_validation("Candidate does not have a name.", "name_present")
        if not candidate.company_domain and not candidate.company_name:
            return fail_validation(
                "Candidate needs either a company domain or company name.",
                "company_domain_or_name_present",
            )
        # For now, we'll consider this good enough to pass validation
        candidate.pass_validation(
            signals=["name_present", "company_domain_or_name_present"],
            resulting_score=75,
        )

        return ProductValidationResult(
            candidate=candidate, message="Validation not implemented yet."
        )

    @activity.defn
    async def check_product_duplicates(
        self, candidate: ProductCandidate | dict
    ) -> List[PotentialDuplicate]:
        """Checks for potential duplicates of a product candidate."""
        if not self.product_resolver:
            self.logger.warning(
                "Entity resolver not configured. Skipping duplicate check."
            )
            return []
        reference = ProductReference(
            value=candidate.name,
            product_name=candidate.name,
            company_domain=candidate.company_domain,
            company_name=candidate.company_name,
        )
        if candidate.company_name:
            if not candidate.name.startswith(candidate.company_name):
                reference.value = f"{candidate.company_name} | {candidate.name}"

        # To improve this, if the company_name isn't present, but the domain is, let's
        # use the resolver to get the company name from the database, and then add the name.

        result = await self.product_resolver.resolve_product(
            reference=reference,
            min_confidence_score=0.85,
        )
        if result.resolved_product and not result.is_ambiguous:
            self.logger.info(
                f"Found existing product: {result.resolved_product.product_name} ({result.resolved_product.id})"
            )
            return [
                PotentialDuplicate(
                    confidence_score=result.confidence_score,
                    shared_product_id=result.resolved_product.id,
                    tenant_product_id=None,
                )
            ]
        elif result.resolved_product:
            dups = [
                PotentialDuplicate(
                    shared_product_id=result.resolved_product.id,
                    confidence_score=result.confidence_score,
                )
            ]
            for match in result.alternative_matches:
                dups.append(
                    PotentialDuplicate(
                        shared_product_id=match.product.id,
                        confidence_score=result.confidence_score,
                    )
                )
            return dups
        elif result.alternative_matches:
            dups = [
                PotentialDuplicate(
                    shared_product_id=match.product.id,
                    confidence_score=result.confidence_score,
                )
                for match in result.alternative_matches
            ]
            return dups
        self.logger.info(
            f"No existing product found for {reference.value}. Passed de-duplication."
        )
        return []

    async def normalize_field_values(
        self, field_values: Dict[str, Any]
    ) -> Dict[str, FieldNormalizationResult]:
        if not field_values:
            return {}

        results = {}
        for field_name, field_value in field_values.items():
            if field_name not in self.normalizers:
                results[field_name] = FieldNormalizationResult(
                    field_name=field_name,
                    input=field_value,
                    output=field_value,
                    review_state="valid",
                )
            else:
                normalizer = self.normalizers[field_name]
                result = normalizer.normalize(field_value)
                results[field_name] = result
        return results

    # Helpers

    def _build_field_dicts(
        self, candidate: ProductCandidate | ProductCandidateDatapoints
    ):
        """Builds the field dictionaries for a product candidate or datapoint candidates based on their normalization state."""
        normalized_fields = {}
        invalid_fields = {}
        pending_fields = {}
        for field_name, field_value in candidate.field_values.items():
            if status := candidate.field_normalization_state.get(field_name):
                if status == "valid":
                    normalized_fields[field_name] = field_value
                elif status == "invalid":
                    invalid_fields[field_name] = field_value
                elif status == "pending":
                    pending_fields[field_name] = field_value
                elif status == "failed":
                    pending_fields[field_name] = field_value
                    self.logger.info(
                        "Field %s is marked as failed, re-normalizing...",
                        field_name,
                    )
            else:
                # Assume it's 'pending' if not explicitly set
                pending_fields[field_name] = field_value
                candidate.field_normalization_state[field_name] = "pending"
        return [normalized_fields, invalid_fields, pending_fields]


# Testing


async def test_normalization():
    from core.db import DatabaseManager
    from app.services.products.entity_resolution.service import ProductEntityResolver
    from app.services.products.storage.products import ProductStorageService
    from app.services.products.search.service import ProductSearchService
    from app.services.companies.entity_resolution.service import CompanyEntityResolver
    from app.services.companies.search.service import CompanySearchService
    from app.services.companies.storage.companies import CompanyStorageService

    db = DatabaseManager()
    db.initialize(
        write_url="postgresql://dev:password@localhost:5432/doro_db",
        read_url="postgresql://reader:read0nlyPass@localhost:5432/doro_db",
    )
    company_resolver = CompanyEntityResolver(
        storage_service=CompanyStorageService(db),
        search_service=CompanySearchService(db),
    )
    resolver = ProductEntityResolver(
        storage_service=ProductStorageService(db),
        search_service=ProductSearchService(db),
        company_resolver=company_resolver,
    )
    service = ProductNormalizationService(product_resolver=resolver)
    test_cases = [
        {
            "name": "iPhone",
            "company_domain": "Apple",  # Invalid domain
            "description": "A smartphone",
        },
        {
            "name": "iPhone",
            "company_domain": "apple.com",  # Valid domain
            "description": "A smartphone",
        },
        {
            "name": "Macbook Pro",
            # "company_domain": "apple.com",
            "company_name": "Apple",
        },
    ]
    for test_case in test_cases:
        candidate = ProductCandidate(
            field_values=test_case,
            confidence_scores={k: 0.6 for k in test_case.keys()},
            # field_normalization_state={k: "pending" for k in test_case.keys()},
        )
        candidate, potential_duplicates = (
            await service.normalize_and_verify_product_candidate(candidate)
        )
        print(candidate)
        print(potential_duplicates)
        print("Is ready to index?", candidate.ready_to_index)


if __name__ == "__main__":
    import asyncio

    asyncio.run(test_normalization())

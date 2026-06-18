from pydantic import (
    BaseModel,
    Field,
    field_serializer,
    field_validator,
    computed_field,
    HttpUrl,
)
from uuid import UUID
from datetime import datetime
from typing import Optional, List, Union, Literal, get_args
from core.schemas.categorical_fields import (
    PrimaryIndustryLiteral as PrimaryIndustry,
    LifecycleCategoryLiteral as LifecycleCategory,
    OfferingCategoryLiteral as OfferingCategory,
)
from core.services.validation import BaseValidator
from core.lib.companies import get_favicon_url
from core.schemas.base import CommonSerializersMixin
from core.schemas.exists import StorageLocation, ExistsResponse


class Config:
    minimum_validation_score = 70
    """The minimum score required for a company to be considered 'verified', to include in API responses, etc."""


# Field definitions with reusable examples, descriptions, and validation
class Fields:
    """Centralized field definitions for consistent reuse across models."""

    @staticmethod
    def id(description: Optional[str] = None) -> dict:
        return {
            "description": description or "Unique identifier",
            "examples": ["123e4567-e89b-12d3-a456-426614174000"],
            "has_datapoints": False,
        }

    @staticmethod
    def domain(description: Optional[str] = None) -> dict:
        base_desc = (
            description
            or "The domain of the company. This is the primary identifier for the company."
        )
        return {
            "description": base_desc,
            "examples": ["x.com", "apple.com", "aws.amazon.com"],
            "has_datapoints": False,
        }

    @staticmethod
    def name(description: Optional[str] = None) -> dict:
        return {
            "description": description or "The colloquial name of the company.",
            "examples": ["X", "Apple", "AWS"],
            "has_datapoints": True,
        }

    @staticmethod
    def description() -> dict:
        return {
            "description": "A brief description of the company and what they do.",
            "examples": [
                "A social media company that specializes in microblogging and social networking.",
                "A large, established software company that specializes search and advertising.",
                "A large consumer hardware company that designs and sells consumer electronics.",
                "A large cloud computing company that provides a wide range of cloud services.",
            ],
            "has_datapoints": True,
        }

    @staticmethod
    def alt_names() -> dict:
        return {
            "description": "Alternative names for the company.",
            "examples": [["Twitter"], ["IBM, International Business Machines"]],
            "has_datapoints": True,
        }

    @staticmethod
    def legal_name() -> dict:
        return {
            "description": "The legal name of the company.",
            "examples": [
                "X, Inc.",
                "Google LLC",
                "Apple Inc.",
                "Amazon Web Services, Inc.",
            ],
            "has_datapoints": True,
        }

    @staticmethod
    def founding_year() -> dict:
        return {
            "description": "The year the company was founded.",
            "examples": [1976, 1971, 1994],
            "has_datapoints": True,
        }

    @staticmethod
    def alt_domains() -> dict:
        return {
            "description": "Alternative domains for the company.",
            "examples": [["twitter.com", "x.co.uk"], ["apple.com", "apple.co.uk"]],
            "has_datapoints": True,
        }

    # @staticmethod
    # def previous_domains() -> dict:
    #     return {
    #         "description": "Any prior domains of the company.",
    #         "examples": [["twitter.com"]],
    #         "has_datapoints": False,
    #     }

    # @staticmethod
    # def previous_names() -> dict:
    #     return {
    #         "description": "Any prior names of the company.",
    #         "examples": [["Twitter"]],
    #         "has_datapoints": False,
    #     }

    @staticmethod
    def stock_ticker() -> dict:
        return {
            "description": "The stock ticker of the company, not including the exchange.",
            "examples": [None, "GOOGL", "AAPL", "AMZN"],
            "has_datapoints": True,
        }

    @staticmethod
    def location() -> dict:
        return {
            "description": "The location of the company's headquarters.",
            "examples": ["San Francisco, CA", "New York, NY", "Seattle, WA"],
            "has_datapoints": True,
        }

    @staticmethod
    def specialties() -> dict:
        return {
            "description": "The specialties of the company.",
            "examples": [
                ["Social Media", "News", "Digital Advertising"],
                "Hardware",
                "Cloud",
                "AI",
                "Machine Learning",
            ],
            "has_datapoints": True,
        }

    @staticmethod
    def primary_industry() -> dict:
        return {
            "description": """The primary industry category that a company belongs to.

    This should capture vertical or sector the company operates in,
    not necessarily the products / services it offers.""",
            "examples": list(get_args(PrimaryIndustry)),
            "has_datapoints": True,
        }

    @staticmethod
    def offering_category() -> dict:
        return {
            "description": "What type of products or services the company offers.",
            "examples": list(get_args(OfferingCategory)),
            "has_datapoints": True,
        }

    @staticmethod
    def lifecycle_stage() -> dict:
        return {
            "description": "What stage the company is in its lifecycle.",
            "examples": list(get_args(LifecycleCategory)),
            "has_datapoints": True,
        }

    @staticmethod
    def is_multi_product() -> dict:
        return {
            "description": "Whether the company offers multiple products or services.",
            "examples": [True, False],
            "has_datapoints": True,
        }

    @staticmethod
    def primary_product_id() -> dict:
        return {
            "description": "The ID to the 'product' that is the primary product of the company. Does not need to be set for all companies.",
            "examples": ["123e4567-e89b-12d3-a456-426614174000"],
            "has_datapoints": True,
        }

    @staticmethod
    def datetime(required: bool = True) -> dict:
        return {
            "description": "A datetime value.",
            "examples": ["2025-05-25T00:00:00Z"],
        }

    @staticmethod
    def logo_url() -> dict:
        return {
            "description": "The URL of the company's logo.",
            "examples": [
                "https://www.x.com/i/about/brand-guidelines/logo",
                "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
            ],
            "has_datapoints": False,
        }

    @staticmethod
    def favicon_url_computed_field():
        """Returns the computed field definition for favicon_url."""
        return computed_field(
            return_type=str,
            description="The URL of the company's favicon.",
            examples=[
                "https://www.google.com/s2/favicons?domain=x.com&sz=256",
                "https://www.google.com/s2/favicons?domain=doro.io&sz=256",
            ],
        )

    @staticmethod
    def website_url_computed_field():
        """Returns the computed field definition for website_url."""
        return computed_field(
            return_type=str,
            description="The URL of the company's website homepage.",
            examples=["https://www.x.com", "https://www.doro.io"],
        )

    @staticmethod
    def website_url() -> dict:
        return {
            "description": "The URL of the company's website homepage.",
            "examples": ["https://www.x.com", "https://www.doro.io"],
            "has_datapoints": True,
        }

    @staticmethod
    def linkedin_url() -> dict:
        return {
            "description": "The URL of the company's LinkedIn page.",
            "examples": [
                "https://www.linkedin.com/company/twitter",
                "https://www.linkedin.com/company/google",
            ],
            "has_datapoints": True,
        }

    @staticmethod
    def wikipedia_url() -> dict:
        return {
            "description": "The URL of the company's Wikipedia page.",
            "examples": [
                "https://en.wikipedia.org/wiki/Twitter",
                "https://en.wikipedia.org/wiki/Google",
            ],
            "has_datapoints": True,
        }

    @staticmethod
    def pitchbook_url() -> dict:
        return {
            "description": "The URL of the company's Pitchbook page.",
            "examples": ["https://pitchbook.com/profiles/company/x"],
            "has_datapoints": True,
        }

    @staticmethod
    def x_url() -> dict:
        return {
            "description": "The URL of the company's X (Twitter) page.",
            "examples": ["https://x.com/x"],
            "has_datapoints": True,
        }

    @staticmethod
    def parent_company() -> dict:
        return {
            "description": "The name of the parent company of the company (if applicable).",
            "examples": ["Alphabet"],
            "has_datapoints": True,
        }

    @staticmethod
    def competitors() -> dict:
        return {
            "description": "The names of the companies closest competitors.",
            "examples": ["TikTok", "Facebook", "Instagram"],
            "has_datapoints": True,
        }

    @staticmethod
    def competitors_object() -> dict:
        return {
            "description": "The companies closest competitors. If the competitor is indexed on our platform, we'll return an object with the company's ID, domain, name, and favicon for display. If the competitor is not indexed on our platform, we'll return the name of the competitor.",
            "examples": [
                [
                    IdentifiedCompany(
                        id=UUID("123e4567-e89b-12d3-a456-426614174000"),
                        domain="tiktok.com",
                        name="TikTok",
                    ),
                    "Facebook",
                ],
            ],
            "has_datapoints": True,
        }

    @staticmethod
    def parent_company_object() -> dict:
        return {
            "description": "The parent company of the company (if applicable). If the parent company is indexed on our platform, we'll return an object with the company's ID, domain, name, and favicon for display. If the parent company is not indexed on our platform, we'll return the name of the parent company.",
            "examples": [
                IdentifiedCompany(
                    id=UUID("123e4567-e89b-12d3-a456-426614174002"),
                    domain="abc.xyz",
                    name="Alphabet",
                )
            ],
            "has_datapoints": True,
        }

    @staticmethod
    def identity_validation_score() -> dict:
        return {
            "description": "Our confidence that this is a 'real' company.",
            "examples": [85, 90, 60],
            "ge": 0,
            "le": 100,
            "has_datapoints": False,
        }

    @staticmethod
    def last_validated_time() -> dict:
        return {
            "description": "The time the company was last validated.",
            "examples": ["2024-01-15T10:00:00Z"],
            "has_datapoints": False,
        }

    @staticmethod
    def validation_metadata() -> dict:
        return {
            "description": "Info about validation signals used to build the confidence score.",
            "examples": [
                {
                    "last_validated": "2024-01-15T10:00:00Z",
                    "signals": {
                        "domain_resolves": {
                            "success": True,
                            "boost": 30,
                            "checked": "2024-01-15T10:00:00Z",
                        },
                        "llm_check": {
                            "success": True,
                            "boost": 40,
                            "checked": "2024-01-15T10:00:01Z",
                        },
                        "ssl_scrape": {
                            "success": True,
                            "boost": 0,
                            "error": "captcha",
                            "checked": "2024-01-15T10:00:02Z",
                        },
                    },
                }
            ],
        }

    @staticmethod
    def source_summary() -> dict:
        return {
            "description": "Summary of the sources used to build the company.",
            "examples": [
                SourceSummary(
                    last_sourced=datetime.now(),
                    last_reconciled=datetime.now(),
                    strategies_used=[
                        SourceStrategyUsed(
                            id=UUID("123e4567-e89b-12d3-a456-426614174000"),
                            name="Sourcescrub",
                            last_used=datetime.now(),
                        )
                    ],
                )
            ],
            "has_datapoints": False,
        }

    @staticmethod
    def storage_location() -> dict:
        return {
            "description": "The type of storage that the company is stored in.",
            "examples": ["shared", "tenant", "both"],
            "has_datapoints": False,
        }

    class FieldSets:
        @staticmethod
        def minimal() -> List[str]:
            return [
                "id",
                "domain",
                "name",
                "is_verified",
            ]

        @staticmethod
        def standard() -> List[str]:
            return Fields.FieldSets.minimal() + [
                "description",
                "legal_name",
                "location",
                "stock_ticker",
                "alt_names",
                "alt_domains",
                "specialties",
                "founding_year",
                "primary_industry",
                "offering_category",
                "lifecycle_stage",
                "website_url",
                "identity_validation_score",
            ]

        @staticmethod
        def full() -> List[str]:
            return Fields.FieldSets.standard() + [
                "logo_url",
                "linkedin_url",
                "wikipedia_url",
                "pitchbook_url",
                "x_url",
                "primary_product_id",
                "is_multi_product",
                "competitors",
                "parent_company",
                "products",
                "validation_metadata",
                "last_validated_time",
            ]

        @staticmethod
        def computed() -> List[str]:
            return [
                "id",
                "favicon_url",
                "created_time",
                "last_updated_time",
                "is_verified",
                "identity_validation_score",
                "last_validated_time",
                "validation_metadata",
            ]

        @staticmethod
        def relationships() -> List[str]:
            return [
                "competitors",
                "parent_company",
            ]

        @staticmethod
        def lists() -> List[str]:
            return [
                "competitors",
                "alt_names",
                "alt_domains",
                "specialties",
                "tags",
            ]

        @staticmethod
        def identifiers() -> List[str]:
            """Used in the StableCompanyIdentifier class."""
            return [
                "domain",
                "name",
                "alt_names",
                "alt_domains",
            ]


# Common mixins for shared functionality
class CommonValidatorsMixin:
    """Shared validators that can be mixed into models."""

    @field_validator("domain")
    @classmethod
    def validate_domain(cls, v: str):
        return BaseValidator.validate_domain(v)

    @field_validator("alt_domains")
    @classmethod
    def validate_domain_lists(cls, v: List[str]):
        return [BaseValidator.validate_domain(d) for d in v]


# Core models with explicit field ordering
class IdentifiedCompany(BaseModel, CommonSerializersMixin):
    """A company with a verified domain and name that has been uniquely identified and added to the Doro platform."""

    # Core identification fields
    id: UUID = Field(..., **Fields.id())
    "The ID of the company."
    domain: str = Field(..., **Fields.domain())
    "The domain of the company. This is the primary identifier for the company."
    name: str = Field(..., **Fields.name())
    "The colloquial name of the company."

    @Fields.favicon_url_computed_field()
    @property
    def favicon_url(self) -> str:
        return get_favicon_url(self.domain, "256")

    @field_serializer("id", when_used="always")
    def serialize_id(self, v: UUID) -> str:
        return self.serialize_uuid_field(v)


class StableCompanyIdentifier(BaseModel):
    domain: str
    "The domain of the company. This is the primary identifier for the company."
    name: str
    "The primary colloquial name of the company. E.g. 'Apple', 'X', or 'Google'."
    alt_names: List[str] = Field(default_factory=list)
    "Alternative names for the company. E.g. ['Twitter'] for 'X'."
    alt_domains: List[str] = Field(default_factory=list)
    "Alternative domains for the company. E.g. ['twitter.com'] for 'X'."


ReferenceTypeHint = Literal["name", "domain", "uuid"]


class CompanyReference(BaseModel):
    """A reference to a company that needs to be resolved."""

    value: str
    """The raw reference value - could be a name (e.g., "Google"), a domain (e.g., "google.com"), or even a UUID string."""
    type_hint: Optional[ReferenceTypeHint] = None
    """Optional hint about what type of reference this is."""
    # For structured data from normalization
    id: Optional[UUID] = None
    """If available, the company ID from structured data."""
    name: Optional[str] = None
    """If available, the company name from structured data."""
    domain: Optional[str] = None
    """If available, the company domain from structured data."""
    alt_names: Optional[List[str]] = None
    """If available, alternative names for the company from structured data."""
    alt_domains: Optional[List[str]] = None
    """If available, alternative domains for the company from structured data."""


class ResolutionContext(BaseModel):
    """Optional context to improve resolution accuracy."""

    field_name: Optional[str] = None
    """The field being resolved (e.g., 'company', 'competitors', 'investors', etc)."""
    source_company: Optional[IdentifiedCompany] = None
    """The company whose relationships we're resolving (helps with competitor / investor mapping)."""
    utterance_context: Optional[str] = None
    """Surrounding text from a meeting transcript or document."""

    @property
    def is_empty(self) -> bool:
        """Whether the context is empty."""
        return (
            not self.field_name
            and not self.source_company
            and not self.utterance_context
        )

    def model_dump(self, *, exclude_none: bool = True, **kwargs):
        """Override model_dump to exclude None values by default."""
        return super().model_dump(exclude_none=exclude_none, **kwargs)


class ResolvedCompany(BaseModel, CommonSerializersMixin):
    """A canonical company entity that was resolved from a reference."""

    id: UUID
    """The ID of the company that was resolved.

    If the company exists in the shared database, this will be the ID of the company in the `public.shared_companies` table.
    If the company exists in a tenant database, this will be the ID of the company in the `public.tenant_companies` table.
    If it exists in both, this will be the ID of the company in the `public.tenant_companies` table. The ID to the tenant company will be in the `tenant_id` field.
    """
    domain: str
    """The domain of the company that was resolved."""
    name: str
    """The name of the company that was resolved."""
    alt_names: List[str] = Field(default_factory=list)
    """Alternative names for the company that were resolved."""
    alt_domains: List[str] = Field(default_factory=list)
    """Alternative domains for the company that were resolved."""
    source_location: StorageLocation
    """Which database(s) the company was resolved from."""
    source_slug: Optional[str] = None
    """The tenant database slug of the company that was resolved, if it was resolved from a tenant database."""
    tenant_id: Optional[UUID] = None
    """The ID of the company in the tenant database, if it was resolved in a tenant database."""

    @property
    def is_tenant_specific(self) -> bool:
        """Whether the company is only in the tenant database, not the shared database."""
        return self.source_location == StorageLocation.TENANT

    @property
    def is_shared_specific(self) -> bool:
        """Whether the company is only in the shared database, not the tenant database."""
        return self.source_location == StorageLocation.SHARED

    @property
    def favicon_url(self) -> Optional[str]:
        """The logo URL of the company that was resolved."""
        return get_favicon_url(self.domain)

    def as_stable_identifier(self) -> StableCompanyIdentifier:
        """Convert the resolved company to a stable identifier."""
        return StableCompanyIdentifier(
            domain=self.domain,
            name=self.name,
            alt_names=self.alt_names,
            alt_domains=self.alt_domains,
        )

    def as_company_exists_response(self) -> ExistsResponse:
        """Convert the resolved company to a company exists response."""
        in_shared = (
            self.source_location == StorageLocation.SHARED
            or self.source_location == StorageLocation.BOTH
        )
        in_tenant = (
            self.source_location == StorageLocation.TENANT
            or self.source_location == StorageLocation.BOTH
        )

        return ExistsResponse(
            in_shared=in_shared,
            in_tenant=in_tenant,
            shared_id=self.id if in_shared else None,
            tenant_id=self.tenant_id if in_tenant else None,
        )

    def as_identified_company(self) -> IdentifiedCompany:
        """Convert the resolved company to an identifiable company."""
        return IdentifiedCompany(
            id=self.id,
            domain=self.domain,
            name=self.name,
        )

    def has_all_company_fields(self, field_names: set[str]) -> bool:
        """Whether the resolved company has all the fields in the set."""
        model_fields = [
            "id",
            "domain",
            "name",
            "alt_names",
            "alt_domains",
            "source_location",
            "source_slug",
            "tenant_id",
        ]
        return all(field_name in model_fields for field_name in field_names)

    def as_company_schema(self) -> "Company":
        """Convert the resolved company to a company schema."""
        return Company(
            id=self.id,
            domain=self.domain,
            name=self.name,
            alt_names=self.alt_names,
            alt_domains=self.alt_domains,
            storage_location=self.source_location,
        )

    @field_serializer("source_location", when_used="always")
    def serialize_storage_location(self, v: StorageLocation) -> str:
        return v.value

    @field_serializer("id", "tenant_id", when_used="always")
    def serialize_id(self, v: UUID | None) -> str:
        return self.serialize_uuid_field(v)


class StoredCompanyReference(BaseModel, CommonSerializersMixin):
    reference: CompanyReference
    """The reference that was used to identify the company."""
    resolved_company: Optional[ResolvedCompany] = None
    """The company that was resolved from the reference. Available if we have a non-ambiguous resolution."""
    resolution_last_updated: Optional[datetime] = None
    """The time we last tried to resolve the company reference to a specific company in our database."""

    def model_dump(self, *, exclude_none: bool = True, **kwargs):
        """Override model_dump to exclude None values by default."""
        return super().model_dump(exclude_none=exclude_none, **kwargs)

    @field_serializer("resolution_last_updated", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)


StoredRelatedCompany = Union[StoredCompanyReference, str]
RelatedCompany = Union[IdentifiedCompany, str]


class SourceStrategyUsed(BaseModel, CommonSerializersMixin):
    id: UUID
    name: str
    last_used: datetime

    @field_serializer("last_used", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)

    @field_serializer("id", when_used="always")
    def serialize_id(self, v: UUID) -> str:
        return self.serialize_uuid_field(v)


class SourceSummary(BaseModel, CommonSerializersMixin):
    last_sourced: Optional[datetime] = None
    strategies_used: List[SourceStrategyUsed] = Field(default_factory=list)

    @field_serializer("last_sourced", when_used="always")
    def serialize_datetimes(self, v: datetime) -> str:
        return self.serialize_dt_field(v)


# Company schemas corresponding to the DB models
# These are essentially "cached" outputs of datapoint
# reconciliation / enrichment.


class SharedCompanyCreate(BaseModel, CommonValidatorsMixin, CommonSerializersMixin):
    """Schema for creating a shared company."""

    # Core identification (order: most important first)
    domain: str = Field(..., **Fields.domain())
    "The domain of the company. This is the primary identifier for the company."
    name: str = Field(..., **Fields.name())
    "The colloquial name of the company."

    # Basic information
    description: Optional[str] = Field(None, **Fields.description())
    legal_name: Optional[str] = Field(None, **Fields.legal_name())
    location: Optional[str] = Field(None, **Fields.location())
    stock_ticker: Optional[str] = Field(None, **Fields.stock_ticker())
    founding_year: Optional[int] = Field(None, **Fields.founding_year())

    # Categorical fields
    primary_industry: Optional[PrimaryIndustry] = Field(
        None, **Fields.primary_industry()
    )
    offering_category: Optional[OfferingCategory] = Field(
        None, **Fields.offering_category()
    )
    lifecycle_stage: Optional[LifecycleCategory] = Field(
        None, **Fields.lifecycle_stage()
    )

    # Lists and alternatives
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names())
    alt_domains: Optional[List[str]] = Field(None, **Fields.alt_domains())
    specialties: Optional[List[str]] = Field(None, **Fields.specialties())

    # Product info
    primary_product_id: Optional[UUID] = Field(None, **Fields.primary_product_id())
    is_multi_product: Optional[bool] = Field(None, **Fields.is_multi_product())

    # Relationships
    parent_company: Optional[StoredRelatedCompany] = Field(
        None, **Fields.parent_company()
    )
    competitors: Optional[List[StoredRelatedCompany]] = Field(
        None, **Fields.competitors()
    )

    # URLs
    website_url: Optional[HttpUrl] = Field(None, **Fields.website_url())
    logo_url: Optional[HttpUrl] = Field(None, **Fields.logo_url())
    linkedin_url: Optional[HttpUrl] = Field(None, **Fields.linkedin_url())
    wikipedia_url: Optional[HttpUrl] = Field(None, **Fields.wikipedia_url())
    pitchbook_url: Optional[HttpUrl] = Field(None, **Fields.pitchbook_url())
    x_url: Optional[HttpUrl] = Field(None, **Fields.x_url())

    # Verification fields - Required for creation
    identity_validation_score: int = Field(..., **Fields.identity_validation_score())
    last_validated_time: datetime = Field(..., **Fields.last_validated_time())
    validation_metadata: dict = Field(
        default_factory=dict, **Fields.validation_metadata()
    )

    # Serialization
    @field_serializer(
        "website_url",
        "logo_url",
        "linkedin_url",
        "wikipedia_url",
        "pitchbook_url",
        "x_url",
        when_used="always",
    )
    def serialize_urls(self, v: HttpUrl) -> str:
        return self.serialize_url_field(v)

    @field_serializer("last_validated_time", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)

    @field_serializer("primary_product_id", when_used="always")
    def serialize_uuid(self, v: UUID) -> str:
        return self.serialize_uuid_field(v)


class SharedCompanyUpdate(BaseModel, CommonValidatorsMixin, CommonSerializersMixin):
    """Schema for updating a shared company."""

    # All fields optional for updates, but maintain same order as create
    domain: Optional[str] = Field(None, **Fields.domain())
    "The domain of the company. This is the primary identifier for the company."
    name: Optional[str] = Field(None, **Fields.name())
    "The colloquial name of the company."

    # Basic information
    description: Optional[str] = Field(None, **Fields.description())
    legal_name: Optional[str] = Field(None, **Fields.legal_name())
    location: Optional[str] = Field(None, **Fields.location())
    stock_ticker: Optional[str] = Field(None, **Fields.stock_ticker())
    founding_year: Optional[int] = Field(None, **Fields.founding_year())

    # Categorical fields
    primary_industry: Optional[PrimaryIndustry] = Field(
        None, **Fields.primary_industry()
    )
    offering_category: Optional[OfferingCategory] = Field(
        None, **Fields.offering_category()
    )
    lifecycle_stage: Optional[LifecycleCategory] = Field(
        None, **Fields.lifecycle_stage()
    )

    # Lists and alternatives
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names())
    alt_domains: Optional[List[str]] = Field(None, **Fields.alt_domains())
    specialties: Optional[List[str]] = Field(None, **Fields.specialties())

    # Product info
    primary_product_id: Optional[UUID] = Field(None, **Fields.primary_product_id())
    is_multi_product: Optional[bool] = Field(None, **Fields.is_multi_product())

    # Relationships
    parent_company: Optional[StoredRelatedCompany] = Field(
        None, **Fields.parent_company()
    )
    competitors: Optional[List[StoredRelatedCompany]] = Field(
        None, **Fields.competitors()
    )

    # URLs
    website_url: Optional[HttpUrl] = Field(None, **Fields.website_url())
    logo_url: Optional[HttpUrl] = Field(None, **Fields.logo_url())
    linkedin_url: Optional[HttpUrl] = Field(None, **Fields.linkedin_url())
    wikipedia_url: Optional[HttpUrl] = Field(None, **Fields.wikipedia_url())
    pitchbook_url: Optional[HttpUrl] = Field(None, **Fields.pitchbook_url())
    x_url: Optional[HttpUrl] = Field(None, **Fields.x_url())

    # Verification fields
    identity_validation_score: Optional[int] = Field(
        None, **Fields.identity_validation_score()
    )
    last_validated_time: Optional[datetime] = Field(
        None, **Fields.last_validated_time()
    )
    validation_metadata: Optional[dict] = Field(None, **Fields.validation_metadata())
    source_summary: Optional[SourceSummary] = Field(None, **Fields.source_summary())

    # Serialization
    @field_serializer(
        "website_url",
        "logo_url",
        "linkedin_url",
        "wikipedia_url",
        "pitchbook_url",
        "x_url",
        when_used="always",
    )
    def serialize_urls(self, v: HttpUrl) -> str:
        return self.serialize_url_field(v)

    @field_serializer("last_validated_time", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)

    @field_serializer("primary_product_id", when_used="always")
    def serialize_uuid(self, v: UUID) -> str:
        return self.serialize_uuid_field(v)


class SharedCompany(BaseModel, CommonSerializersMixin):
    """A shared company with full data and metadata."""

    # System fields first
    id: UUID = Field(..., **Fields.id(description="The ID of the shared company."))
    created_time: datetime = Field(..., **Fields.datetime())
    last_updated_time: datetime = Field(..., **Fields.datetime())

    # Core identification
    domain: str = Field(..., **Fields.domain())
    "The domain of the company. This is the primary identifier for the company."
    name: str = Field(..., **Fields.name())
    "The colloquial name of the company."

    # Basic information
    description: Optional[str] = Field(None, **Fields.description())
    legal_name: Optional[str] = Field(None, **Fields.legal_name())
    location: Optional[str] = Field(None, **Fields.location())
    stock_ticker: Optional[str] = Field(None, **Fields.stock_ticker())
    founding_year: Optional[int] = Field(None, **Fields.founding_year())

    # Categorical fields
    primary_industry: Optional[PrimaryIndustry] = Field(
        None, **Fields.primary_industry()
    )
    offering_category: Optional[OfferingCategory] = Field(
        None, **Fields.offering_category()
    )
    lifecycle_stage: Optional[LifecycleCategory] = Field(
        None, **Fields.lifecycle_stage()
    )

    # Lists and alternatives
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names())
    alt_domains: Optional[List[str]] = Field(None, **Fields.alt_domains())
    specialties: Optional[List[str]] = Field(None, **Fields.specialties())

    # Product info
    primary_product_id: Optional[UUID] = Field(None, **Fields.primary_product_id())
    is_multi_product: Optional[bool] = Field(None, **Fields.is_multi_product())

    # URLs
    website_url: Optional[HttpUrl] = Field(None, **Fields.website_url())
    logo_url: Optional[HttpUrl] = Field(None, **Fields.logo_url())
    linkedin_url: Optional[HttpUrl] = Field(None, **Fields.linkedin_url())
    wikipedia_url: Optional[HttpUrl] = Field(None, **Fields.wikipedia_url())
    pitchbook_url: Optional[HttpUrl] = Field(None, **Fields.pitchbook_url())
    x_url: Optional[HttpUrl] = Field(None, **Fields.x_url())

    # Verification fields
    identity_validation_score: int = Field(..., **Fields.identity_validation_score())
    last_validated_time: Optional[datetime] = Field(
        None, **Fields.last_validated_time()
    )
    validation_metadata: Optional[dict] = Field(None, **Fields.validation_metadata())
    source_summary: Optional[SourceSummary] = Field(None, **Fields.source_summary())

    # Relationships (optional includes)
    competitors: Optional[List[RelatedCompany]] = Field(
        None, **Fields.competitors_object()
    )
    parent_company: Optional[RelatedCompany] = Field(
        None, **Fields.parent_company_object()
    )
    discovery_metadata: Optional[dict] = Field(
        None,
        description="Metadata about how the company was discovered.",
    )

    @field_serializer("id", "primary_product_id", when_used="always")
    def serialize_id(self, v: UUID) -> str:
        return self.serialize_uuid_field(v)

    @field_serializer(
        "created_time",
        "last_updated_time",
        "last_validated_time",
        when_used="always",
    )
    def serialize_datetimes(self, v: datetime) -> str:
        return self.serialize_dt_field(v)

    @field_serializer(
        "website_url",
        "logo_url",
        "linkedin_url",
        "wikipedia_url",
        "pitchbook_url",
        "x_url",
        when_used="always",
    )
    def serialize_urls(self, v: HttpUrl) -> str:
        return self.serialize_url_field(v)

    # Computed fields
    @computed_field
    @property
    def is_verified(self) -> bool:
        return self.identity_validation_score >= Config.minimum_validation_score

    @Fields.favicon_url_computed_field()
    @property
    def favicon_url(self) -> str:
        return get_favicon_url(self.domain, "256")

    def to_identified_company(self) -> IdentifiedCompany:
        return IdentifiedCompany(
            id=self.id,
            domain=self.domain,
            name=self.name,
        )


class TenantCompanyCreate(BaseModel, CommonValidatorsMixin, CommonSerializersMixin):
    """Schema for creating a tenant-specific company."""

    # Tenant-specific fields first
    shared_company_id: Optional[UUID] = Field(
        None,
        **Fields.id(
            description="The ID of the shared company that this tenant company is associated with.",
        ),
    )
    domain: Optional[str] = Field(
        None,
        **Fields.domain(
            description="The domain of the company. If not included in create, the domain will be inferred from the shared company."
        ),
    )
    "The domain of the company. This is the primary identifier for the company."

    # All other fields follow same pattern as SharedCompanyCreate
    name: Optional[str] = Field(None, **Fields.name())
    "The colloquial name of the company."
    description: Optional[str] = Field(None, **Fields.description())
    legal_name: Optional[str] = Field(None, **Fields.legal_name())
    location: Optional[str] = Field(None, **Fields.location())
    stock_ticker: Optional[str] = Field(None, **Fields.stock_ticker())
    founding_year: Optional[int] = Field(None, **Fields.founding_year())
    primary_industry: Optional[PrimaryIndustry] = Field(
        None, **Fields.primary_industry()
    )
    offering_category: Optional[OfferingCategory] = Field(
        None, **Fields.offering_category()
    )
    lifecycle_stage: Optional[LifecycleCategory] = Field(
        None, **Fields.lifecycle_stage()
    )
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names())
    alt_domains: Optional[List[str]] = Field(None, **Fields.alt_domains())
    specialties: Optional[List[str]] = Field(None, **Fields.specialties())
    website_url: Optional[HttpUrl] = Field(None, **Fields.website_url())
    logo_url: Optional[HttpUrl] = Field(None, **Fields.logo_url())
    linkedin_url: Optional[HttpUrl] = Field(None, **Fields.linkedin_url())
    wikipedia_url: Optional[HttpUrl] = Field(None, **Fields.wikipedia_url())
    pitchbook_url: Optional[HttpUrl] = Field(None, **Fields.pitchbook_url())
    x_url: Optional[HttpUrl] = Field(None, **Fields.x_url())

    # Relationships
    parent_company: Optional[StoredRelatedCompany] = Field(
        None, **Fields.parent_company()
    )
    competitors: Optional[List[StoredRelatedCompany]] = Field(
        None, **Fields.competitors()
    )

    # Verification fields - Required for creation
    identity_validation_score: int = Field(..., **Fields.identity_validation_score())
    last_validated_time: datetime = Field(..., **Fields.last_validated_time())
    validation_metadata: dict = Field(
        default_factory=dict, **Fields.validation_metadata()
    )

    # Serialization
    @field_serializer(
        "website_url",
        "logo_url",
        "linkedin_url",
        "wikipedia_url",
        "pitchbook_url",
        "x_url",
        when_used="always",
    )
    def serialize_urls(self, v: HttpUrl) -> str:
        return self.serialize_url_field(v)

    @field_serializer("last_validated_time", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)


class TenantCompanyUpdate(BaseModel, CommonValidatorsMixin, CommonSerializersMixin):
    """Schema for updating a tenant-specific company."""

    # All fields optional, same order as create
    shared_company_id: Optional[UUID] = Field(
        None,
        **Fields.id(
            description="The ID of the shared company that this tenant company is associated with.",
        ),
    )
    domain: Optional[str] = Field(None, **Fields.domain())
    "The domain of the company. This is the primary identifier for the company."
    name: Optional[str] = Field(None, **Fields.name())
    "The colloquial name of the company."
    description: Optional[str] = Field(None, **Fields.description())
    legal_name: Optional[str] = Field(None, **Fields.legal_name())
    location: Optional[str] = Field(None, **Fields.location())
    stock_ticker: Optional[str] = Field(None, **Fields.stock_ticker())
    founding_year: Optional[int] = Field(None, **Fields.founding_year())
    primary_industry: Optional[PrimaryIndustry] = Field(
        None, **Fields.primary_industry()
    )
    offering_category: Optional[OfferingCategory] = Field(
        None, **Fields.offering_category()
    )
    lifecycle_stage: Optional[LifecycleCategory] = Field(
        None, **Fields.lifecycle_stage()
    )
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names())
    alt_domains: Optional[List[str]] = Field(None, **Fields.alt_domains())
    specialties: Optional[List[str]] = Field(None, **Fields.specialties())
    parent_company: Optional[StoredRelatedCompany] = Field(
        None, **Fields.parent_company()
    )
    competitors: Optional[List[StoredRelatedCompany]] = Field(
        None, **Fields.competitors()
    )
    website_url: Optional[HttpUrl] = Field(None, **Fields.website_url())
    logo_url: Optional[HttpUrl] = Field(None, **Fields.logo_url())
    linkedin_url: Optional[HttpUrl] = Field(None, **Fields.linkedin_url())
    wikipedia_url: Optional[HttpUrl] = Field(None, **Fields.wikipedia_url())
    pitchbook_url: Optional[HttpUrl] = Field(None, **Fields.pitchbook_url())
    x_url: Optional[HttpUrl] = Field(None, **Fields.x_url())

    # Verification fields
    identity_validation_score: Optional[int] = Field(
        None, **Fields.identity_validation_score()
    )
    last_validated_time: Optional[datetime] = Field(
        None, **Fields.last_validated_time()
    )
    validation_metadata: Optional[dict] = Field(None, **Fields.validation_metadata())
    source_summary: Optional[SourceSummary] = Field(None, **Fields.source_summary())

    # Serialization
    @field_serializer(
        "website_url",
        "logo_url",
        "linkedin_url",
        "wikipedia_url",
        "pitchbook_url",
        "x_url",
        when_used="always",
    )
    def serialize_urls(self, v: HttpUrl) -> str:
        return self.serialize_url_field(v)

    @field_serializer("last_validated_time", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)


class TenantCompany(BaseModel, CommonSerializersMixin):
    """A tenant-specific company with full data and metadata."""

    # System fields first
    id: UUID = Field(..., **Fields.id(description="The ID of the company."))
    created_time: datetime = Field(..., **Fields.datetime())
    last_updated_time: datetime = Field(..., **Fields.datetime())

    # Tenant-specific fields
    shared_company_id: Optional[UUID] = Field(
        None,
        **Fields.id(
            description="The ID of the shared company that this tenant company is associated with.",
        ),
    )
    domain: str = Field(..., **Fields.domain())
    "The domain of the company. This is the primary identifier for the company."

    # All other fields in consistent order
    name: Optional[str] = Field(None, **Fields.name())
    "The colloquial name of the company."
    description: Optional[str] = Field(None, **Fields.description())
    legal_name: Optional[str] = Field(None, **Fields.legal_name())
    location: Optional[str] = Field(None, **Fields.location())
    stock_ticker: Optional[str] = Field(None, **Fields.stock_ticker())
    founding_year: Optional[int] = Field(None, **Fields.founding_year())
    primary_industry: Optional[PrimaryIndustry] = Field(
        None, **Fields.primary_industry()
    )
    offering_category: Optional[OfferingCategory] = Field(
        None, **Fields.offering_category()
    )
    lifecycle_stage: Optional[LifecycleCategory] = Field(
        None, **Fields.lifecycle_stage()
    )
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names())
    alt_domains: Optional[List[str]] = Field(None, **Fields.alt_domains())
    specialties: Optional[List[str]] = Field(None, **Fields.specialties())
    website_url: Optional[HttpUrl] = Field(None, **Fields.website_url())
    logo_url: Optional[HttpUrl] = Field(None, **Fields.logo_url())
    linkedin_url: Optional[HttpUrl] = Field(None, **Fields.linkedin_url())
    wikipedia_url: Optional[HttpUrl] = Field(None, **Fields.wikipedia_url())
    pitchbook_url: Optional[HttpUrl] = Field(None, **Fields.pitchbook_url())
    x_url: Optional[HttpUrl] = Field(None, **Fields.x_url())

    # Verification fields
    identity_validation_score: int = Field(..., **Fields.identity_validation_score())
    last_validated_time: Optional[datetime] = Field(
        None, **Fields.last_validated_time()
    )
    validation_metadata: Optional[dict] = Field(None, **Fields.validation_metadata())
    source_summary: Optional[SourceSummary] = Field(None, **Fields.source_summary())

    # Relationships (optional includes)
    competitors: Optional[List[RelatedCompany]] = Field(
        None, **Fields.competitors_object()
    )
    parent_company: Optional[RelatedCompany] = Field(
        None, **Fields.parent_company_object()
    )
    discovery_metadata: Optional[dict] = Field(
        None,
        description="Metadata about how the company was discovered.",
    )

    # Computed fields

    @computed_field
    @property
    def is_verified(self) -> bool:
        return self.identity_validation_score >= Config.minimum_validation_score

    @Fields.favicon_url_computed_field()
    @property
    def favicon_url(self) -> Optional[str]:
        if not self.domain:
            return None
        return get_favicon_url(self.domain, "256")

    # Serialization

    @field_serializer("id", "shared_company_id", when_used="always")
    def serialize_ids(self, v: UUID) -> str:
        return self.serialize_uuid_field(v)

    @field_serializer(
        "created_time",
        "last_updated_time",
        "last_validated_time",
        when_used="always",
    )
    def serialize_datetimes(self, v: datetime) -> str:
        return self.serialize_dt_field(v)

    @field_serializer(
        "website_url",
        "logo_url",
        "linkedin_url",
        "wikipedia_url",
        "pitchbook_url",
        "x_url",
        when_used="always",
    )
    def serialize_urls(self, v: HttpUrl) -> str:
        return self.serialize_url_field(v)

    def to_identified_company(self) -> IdentifiedCompany:
        return IdentifiedCompany(
            id=self.id,
            domain=self.domain,
            name=self.name,
        )


# Primary company schema - results of reconciling all available datapoints
# from the shared company and tenant company schemas.


class Company(SharedCompany):
    """A company with full data and metadata. These are only returned when a company is found in the database and has been verified."""

    # Same schema as SharedCompany.
    storage_location: StorageLocation = Field(..., **Fields.storage_location())

    def to_string(self, include_details: bool = False) -> str:
        ret_string = f"{self.name} ({self.domain})"
        if not include_details:
            return ret_string
        if self.storage_location == "shared":
            ret_string += " (From shared)"
        elif self.storage_location == "tenant":
            ret_string += " (From tenant)"
        else:
            ret_string += " (Merged from both shared and tenant)"
        if self.location:
            ret_string += f" - {self.location}"
        if self.stock_ticker:
            ret_string += f" - {self.stock_ticker}"
        if self.founding_year:
            ret_string += f" - {self.founding_year}"
        if self.description:
            ret_string += f" - {self.description}"
        return ret_string

    def to_identified_company(self) -> IdentifiedCompany:
        return IdentifiedCompany(
            id=self.id,
            domain=self.domain,
            name=self.name,
        )

    @field_serializer("storage_location", when_used="always")
    def serialize_storage_location(self, v: StorageLocation) -> str:
        return v.value

from pydantic import (
    BaseModel,
    Field,
    field_serializer,
)
from uuid import UUID
from datetime import datetime
from typing import Optional, List, Literal, Dict, Any
from core.schemas.base import CommonSerializersMixin
from core.schemas.exists import StorageLocation
from core.schemas.companies import ResolvedCompany


# For now, just strings. Will turn into Literals / Enums once we know how we want to standardize.
ProductStatus = str  # "in_development", "active", "deprecated", "discontinued"
ProductArchetype = str  # "saas", "dev_tool", "hardware", "cpg_retail", "media", "financial", "other"
ProductGranularityClass = str  # "product", "suite", "model", "pricing_plan", "platform_port", "variant_sku"


class Fields:
    """Centralized field definitions for consistent reuse across models."""

    id = {
        "description": "The unique identifier for the product.",
        "examples": ["123e4567-e89b-12d3-a456-426614174000"],
    }
    company_id = {
        "description": "The unique identifier for the company that the product belongs to.",
        "examples": ["123e4567-e89b-12d3-a456-426614174000"],
    }
    company_domain = {
        "description": "The domain of the company that the product belongs to.",
        "examples": ["apple.com", "google.com"],
    }
    company_name = {
        "description": "The name of the company that the product belongs to.",
        "examples": ["Apple", "Google"],
    }
    company_favicon_url = {
        "description": "The URL of the company's favicon.",
        "examples": ["https://www.apple.com/favicon.ico"],
    }
    product_name = {
        "description": "The name of the product.",
        "examples": ["iPhone 16", "Excel", "F-150"],
    }
    alt_names = {
        "description": "Alternative names for the product.",
        "examples": [[]],
    }
    archetype = {
        "description": "How this product is 'realized' in the world.",
        "examples": ["hardware", "dev_tool", "saas", "cpg_retail", "media", "financial", "other"],
    }
    granularity_class = {
        "description": "A label describing where in a product hierarchy this product fits.",
        "examples": ["model", "suite", "product", "pricing_plan", "platform_port", "variant_sku"],
    }
    parent_product_id = {
        "description": "The unique identifier for the parent product of this product.",
        "examples": ["123e4567-e89b-12d3-a456-426614174000"],
    }
    parent_product_name = {
        "description": "The name of the parent product of this product.",
        "examples": ["iPhone", "Google Workspace"],
    }
    # is_individually_purchasable = {
    #     "description": "Is this a 'shippable offering' - e.g. users can buy / subscribe to / download it. Should be true for most products. If false, likely has a 'parent' product.",
    #     "examples": [True, False],
    # }
    product_description = {
        "description": "A short description of the product.",
        "examples": ["A high-end smartphone known for superior user experience."],
    }
    pricing = {
        "description": "Pricing information for the product.",
        "examples": ["$999"],
    }
    status = {
        "description": "The current status of the product in the market / in its lifecycle.",
        "examples": ["in_development", "active", "deprecated", "discontinued"],
    }
    launched_year = {
        "description": "The year the product was launched.",
        "examples": [2024],
    }
    tags = {
        "description": "Optional descriptive tags about the product.",
        "examples": [
            ["hardware", "consumer electronics"],
            ["software", "productivity"],
        ],
    }
    icon_url = {
        "description": "The URL of the product's icon.",
        "examples": [],
    }
    product_page_url = {
        "description": "The URL of the product's page.",
        "examples": ["https://www.apple.com/iphone-16/"],
    }
    differentiators = {
        "description": "What makes this product unique and better than the competition.",
        "examples": [["Longest battery life of any smartphone", "Best camera of any high-end smartphone"]]
    }
    key_features = {
        "description": "Key features of the product.",
        "examples": [["5G connectivity", "128GB storage", "12MP camera"]],
    }
    target_audiences = {
        "description": "Target audiences for the product.",
        "examples": [["consumer", "high-end"], ["enterprise", "government"]],
    }
    competitor_list = {
        "description": "A list of products (or companies) that are direct competitors to this product.",
        "examples": [["iPhone", "Samsung Galaxy"], ["Microsoft Office", "Google Docs"]],
    }
    created_time = {
        "description": "The time the product was created in the database. Auto-generated. In ISO 8601 format.",
        "examples": ["2025-01-01T00:00:00Z"],
    }
    last_updated_time = {
        "description": "The time the product was last updated in the database. Auto-generated. In ISO 8601 format.",
        "examples": ["2025-01-01T00:00:00Z"],
    }
    storage_location = {
        "description": "Where the product data is stored in Doro.",
        "examples": ["shared", "tenant", "both"],
    }


class StableProductIdentifier(BaseModel):
    name: str = Field(..., **Fields.product_name)
    company_domain: str = Field(..., **Fields.company_domain)
    alt_names: List[str] = Field(default_factory=list, **Fields.alt_names)
    parent_product_name: Optional[str] = Field(None, **Fields.parent_product_name)


ReferenceTypeHint = Literal[
    "name", "uuid", "name_with_company_name", "name_with_company_domain"
]


class ProductReference(BaseModel):
    """A reference to a product that needs to be resolved."""

    value: str
    """The raw reference value - could be a name (e.g. "iPhone"), a name with info about the company as well (e.g. "Apple | iPhone"), or even a UUID string to the specific product."""
    type_hint: Optional[ReferenceTypeHint] = None
    """Optional hint about what type of reference this is."""
    # For structured data from parsing / normalization
    product_name: Optional[str] = None
    """If available, the product name from structured data."""
    product_id: Optional[UUID] = None
    """If available, the product ID from structured data."""
    company_id: Optional[UUID] = None
    """If available, the company ID from structured data."""
    company_domain: Optional[str] = None
    """If available, the company domain from structured data."""
    company_name: Optional[str] = None
    """If available, the company name from structured data."""
    parent_product_name: Optional[str] = None
    """If available, the parent product name from structured data."""
    parent_product_id: Optional[UUID] = None
    """If available, the parent product ID from structured data."""

    def model_dump(self, *, exclude_none: bool = True, **kwargs):
        """Override model_dump to exclude None values by default."""
        return super().model_dump(exclude_none=exclude_none, **kwargs)


class ResolutionContext(BaseModel):
    """Optional context to improve resolution accuracy."""

    relationship_type: Optional[str] = None
    """The type of relationship between the product and the source company (e.g., 'built_by', 'competes_with', etc)."""
    source_company: Optional[ResolvedCompany] = None
    """The company that the referenced product is related to."""
    source_product: Optional["Product"] = None
    """The product that the referenced product is related to."""
    utterance_context: Optional[str] = None
    """Surrounding text from a meeting transcript or document."""

    @property
    def is_empty(self) -> bool:
        """Whether the context is empty."""
        return not any(self.model_dump(exclude_none=True).values())

    def model_dump(self, *, exclude_none: bool = True, **kwargs):
        """Override model_dump to exclude None values by default."""
        return super().model_dump(exclude_none=exclude_none, **kwargs)


class StoredProductReference(BaseModel, CommonSerializersMixin):
    reference: ProductReference
    """The reference that was used to identify the product."""
    resolved_product: Optional["Product"] = None
    """The product that was resolved from the reference. Available if we have a non-ambiguous resolution."""
    resolution_last_updated: Optional[datetime] = None
    """The time we last tried to resolve the product reference to a specific product in our database."""

    def model_dump(self, *, exclude_none: bool = True, **kwargs):
        """Override model_dump to exclude None values by default."""
        return super().model_dump(exclude_none=exclude_none, **kwargs)

    @field_serializer("resolution_last_updated", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)


class SharedProduct(BaseModel, CommonSerializersMixin):
    """Product straight from the shared database with full data and metadata."""

    id: UUID = Field(..., **Fields.id)
    company_id: UUID = Field(..., **Fields.company_id)
    name: str = Field(..., **Fields.product_name)
    "The primary name of the product. This name should be unique within the company, and displayable to the user."

    # Taxonomy
    parent_product_id: Optional[UUID] = Field(None, **Fields.parent_product_id)
    parent_product_name: Optional[str] = Field(None, **Fields.parent_product_name)
    granularity_class: Optional[ProductGranularityClass] = Field(None, **Fields.granularity_class)
    archetype: Optional[ProductArchetype] = Field(None, **Fields.archetype)

    # Basic info
    description: Optional[str] = Field(None, **Fields.product_description)
    pricing: Optional[str] = Field(None, **Fields.pricing)
    status: Optional[ProductStatus] = Field(None, **Fields.status)
    launched_year: Optional[int] = Field(None, **Fields.launched_year)
    tags: Optional[List[str]] = Field(None, **Fields.tags)
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names)
    icon_url: Optional[str] = Field(None, **Fields.icon_url)
    product_page_url: Optional[str] = Field(None, **Fields.product_page_url)

    # Deeper enrichment
    key_features: Optional[List[str]] = Field(None, **Fields.key_features)
    target_audiences: Optional[List[str]] = Field(None, **Fields.target_audiences)
    differentiators: Optional[List[str]] = Field(None, **Fields.differentiators)
    competitor_list: Optional[List[str]] = Field(None, **Fields.competitor_list)

    # Transactional fields
    created_time: datetime = Field(..., **Fields.created_time)
    last_updated_time: datetime = Field(..., **Fields.last_updated_time)

    @field_serializer("id", "company_id", when_used="always")
    def serialize_id_fields(self, v: UUID) -> str:
        return self.serialize_uuid_field(v)

    @field_serializer("created_time", "last_updated_time", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)


class SharedProductCreate(BaseModel, CommonSerializersMixin):
    """Create a product in the shared database."""

    # Required fields
    company_id: UUID = Field(..., **Fields.company_id)
    name: str = Field(..., **Fields.product_name)

    # Optional fields
    parent_product_id: Optional[UUID] = Field(None, **Fields.parent_product_id)
    parent_product_name: Optional[str] = Field(None, **Fields.parent_product_name)
    granularity_class: Optional[ProductGranularityClass] = Field(None, **Fields.granularity_class)
    archetype: Optional[ProductArchetype] = Field(None, **Fields.archetype)
    description: Optional[str] = Field(None, **Fields.product_description)
    pricing: Optional[str] = Field(None, **Fields.pricing)
    status: Optional[ProductStatus] = Field(None, **Fields.status)
    launched_year: Optional[int] = Field(None, **Fields.launched_year)
    tags: Optional[List[str]] = Field(None, **Fields.tags)
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names)
    icon_url: Optional[str] = Field(None, **Fields.icon_url)
    product_page_url: Optional[str] = Field(None, **Fields.product_page_url)
    key_features: Optional[List[str]] = Field(None, **Fields.key_features)
    target_audiences: Optional[List[str]] = Field(None, **Fields.target_audiences)
    differentiators: Optional[List[str]] = Field(None, **Fields.differentiators)
    competitor_list: Optional[List[str]] = Field(None, **Fields.competitor_list)


class SharedProductUpdate(BaseModel, CommonSerializersMixin):
    """Update a product in the shared database."""

    # All fields optional
    company_id: Optional[UUID] = Field(None, **Fields.company_id)
    name: Optional[str] = Field(None, **Fields.product_name)
    parent_product_id: Optional[UUID] = Field(None, **Fields.parent_product_id)
    parent_product_name: Optional[str] = Field(None, **Fields.parent_product_name)
    granularity_class: Optional[ProductGranularityClass] = Field(None, **Fields.granularity_class)
    archetype: Optional[ProductArchetype] = Field(None, **Fields.archetype)
    description: Optional[str] = Field(None, **Fields.product_description)
    pricing: Optional[str] = Field(None, **Fields.pricing)
    status: Optional[ProductStatus] = Field(None, **Fields.status)
    launched_year: Optional[int] = Field(None, **Fields.launched_year)
    tags: Optional[List[str]] = Field(None, **Fields.tags)
    alt_names: Optional[List[str]] = Field(None, **Fields.alt_names)
    icon_url: Optional[str] = Field(None, **Fields.icon_url)
    product_page_url: Optional[str] = Field(None, **Fields.product_page_url)
    key_features: Optional[List[str]] = Field(None, **Fields.key_features)
    target_audiences: Optional[List[str]] = Field(None, **Fields.target_audiences)
    differentiators: Optional[List[str]] = Field(None, **Fields.differentiators)
    competitor_list: Optional[List[str]] = Field(None, **Fields.competitor_list)

# class SharedProduct(BaseModel, CommonSerializersMixin):
#     """Product from the shared database with added attributes inherited from the company."""

#     # Ids first
#     id: UUID = Field(..., **Fields.id)
#     company_id: UUID = Field(..., **Fields.company_id)

#     # Core identification
#     product_name: str = Field(..., **Fields.product_name)
#     "The primary name of the product. This name should be unique within the company, and displayable to the user."
#     company_domain: str = Field(..., **Fields.company_domain)
#     "The domain of the company that the product belongs to."
#     company_name: str = Field(..., **Fields.company_name)
#     "The name of the company that the product belongs to."
#     company_favicon_url: Optional[str] = Field(None, **Fields.company_favicon_url)
#     "The URL of the company's favicon."

#     # Basic info
#     product_description: Optional[str] = Field(None, **Fields.product_description)
#     product_key_features: Optional[List[str]] = Field(None, **Fields.key_features)
#     product_target_audiences: Optional[List[str]] = Field(None, **Fields.target_audiences)
#     product_pricing: Optional[str] = Field(None, **Fields.pricing)
#     product_launched_year: Optional[int] = Field(None, **Fields.launched_year)
#     product_tags: Optional[List[str]] = Field(None, **Fields.tags)
#     product_alt_names: List[str] = Field(default_factory=list, **Fields.alt_names)
#     product_icon_url: Optional[str] = Field(None, **Fields.icon_url)

#     # Transactional fields
#     created_time: datetime = Field(..., **Fields.created_time)
#     last_updated_time: datetime = Field(..., **Fields.last_updated_time)

#     @field_serializer("id", "company_id", when_used="always")
#     def serialize_id_fields(self, v: UUID) -> str:
#         return self.serialize_uuid_field(v)

#     @field_serializer("created_time", "last_updated_time", when_used="always")
#     def serialize_dt(self, v: datetime) -> str:
#         return self.serialize_dt_field(v)


class Product(BaseModel, CommonSerializersMixin):
    """Product with added attributes inherited from the company - sourced from either the shared DB, tenant DB, or combining data from both."""

    # Ids first
    id: UUID = Field(..., **Fields.id)
    company_id: UUID = Field(..., **Fields.company_id)

    # Core identification
    product_name: str = Field(..., **Fields.product_name)
    "The primary name of the product. This name should be unique within the company, and displayable to the user."
    company_domain: str = Field(..., **Fields.company_domain)
    "The domain of the company that the product belongs to."
    company_name: str = Field(..., **Fields.company_name)
    "The name of the company that the product belongs to."
    company_favicon_url: Optional[str] = Field(None, **Fields.company_favicon_url)
    "The URL of the company's favicon."

    # Taxonomy
    parent_product_id: Optional[UUID] = Field(None, **Fields.parent_product_id)
    parent_product_name: Optional[str] = Field(None, **Fields.parent_product_name)
    product_granularity_class: Optional[ProductGranularityClass] = Field(None, **Fields.granularity_class)
    product_archetype: Optional[ProductArchetype] = Field(None, **Fields.archetype)

    # Basic info
    product_description: Optional[str] = Field(None, **Fields.product_description)
    product_pricing: Optional[str] = Field(None, **Fields.pricing)
    product_status: Optional[ProductStatus] = Field(None, **Fields.status)
    product_launched_year: Optional[int] = Field(None, **Fields.launched_year)
    product_tags: Optional[List[str]] = Field(None, **Fields.tags)
    product_alt_names: Optional[List[str]] = Field(None, **Fields.alt_names)
    product_icon_url: Optional[str] = Field(None, **Fields.icon_url)
    product_page_url: Optional[str] = Field(None, **Fields.product_page_url)

    # Deeper enrichment
    product_key_features: Optional[List[str]] = Field(None, **Fields.key_features)
    product_target_audiences: Optional[List[str]] = Field(None, **Fields.target_audiences)
    product_differentiators: Optional[List[str]] = Field(None, **Fields.differentiators)
    product_competitor_list: Optional[List[str]] = Field(None, **Fields.competitor_list)

    # Transactional fields
    storage_location: StorageLocation = Field(..., **Fields.storage_location)
    created_time: datetime = Field(..., **Fields.created_time)
    last_updated_time: datetime = Field(..., **Fields.last_updated_time)

    @field_serializer("id", "company_id", when_used="always")
    def serialize_id_fields(self, v: UUID) -> str:
        return self.serialize_uuid_field(v)

    @field_serializer("created_time", "last_updated_time", when_used="always")
    def serialize_dt(self, v: datetime) -> str:
        return self.serialize_dt_field(v)

    @field_serializer("storage_location", when_used="always")
    def serialize_storage_location(self, v: StorageLocation) -> str:
        return self.serialize_enum(v)

    def stable_identifier(self) -> StableProductIdentifier:
        return StableProductIdentifier(
            name=self.product_name,
            company_domain=self.company_domain,
            alt_names=self.product_alt_names or [],
            parent_product_name=self.parent_product_name,
        )

    def additional_fields(self) -> Dict[str, Any]:
        """Get all fields that are not part of the stable identifier and not null."""
        identifier_fields = set(StableProductIdentifier.model_fields.keys())
        fields = self.model_dump(exclude_none=True)
        return {k: v for k, v in fields.items() if k not in identifier_fields}

    def __str__(self) -> str:
        return f"{self.company_name} - {self.product_name}"

    def to_string(self, include_details: bool = False) -> str:
        if not include_details:
            return f"{self.company_name} - {self.product_name}"
        base = f"{self.company_name} ({self.company_domain}) - {self.product_name}"
        if self.storage_location == "shared":
            base += "\n(From shared database)"
        elif self.storage_location == "tenant":
            base += "\n(From tenant database)"
        else:
            base += "\n(Merged from both shared and tenant databases)"
        if self.product_description:
            base += f"\n Description: {self.product_description[:250]}"
        if self.product_key_features:
            base += f"\n Key Features: {', '.join(self.product_key_features)}"
        if self.product_target_audiences:
            base += f"\n Target Audiences: {', '.join(self.product_target_audiences)}"
        if self.product_pricing:
            base += f"\n Pricing: {self.product_pricing}"
        if self.product_launched_year:
            base += f"\n Launched Year: {self.product_launched_year}"
        if self.product_tags:
            base += f"\n Tags: {', '.join(self.product_tags)}"
        return base

# Reference: Doro product-analysis prompt

Captured verbatim from Doro (via Brian, 2026-05-30). **Not in use yet** — this is the seed for the future `offerings.md` Tier-1 module (deferred). Saved here because it only lived in a chat transcript and is worth not losing. Its granularity rules also informed the `is_multi_product` guidance in [`../../TAXONOMIES.md`](../../TAXONOMIES.md).

---

<product-discovery-prompt>
A product is generally defined as a "shippable offering" users can buy / subscribe to / download. Always rolls up to one company, but has its own identity within the company.

A pricing plan, or a feature, is not a product.

GRANULARITY GUIDELINES:
- Index at the level where FEATURES meaningfully differ between variants
- For consumer hardware: Index at the MODEL level (e.g., 'iPhone 16', 'iPhone 16 Pro') not the product line ('iPhone') or SKU level (storage/color variants)
- For SaaS: Index the main product (e.g., 'Slack') NOT pricing plans / tiers.
- For product suites: Index both the suite AND individual products if they can be purchased/used independently (e.g., 'Microsoft 365' AND 'Excel', 'Word', etc.)
- Use parent_name to show relationships (e.g., 'Excel' has parent 'Microsoft 365')

Our goal with this task is to get a sense of the company's product portfolio - so prioritize breadth across the company over depth within a certain category, product line, or product type.

PRO TIP: The structure of a company's website navigation (flyout menus, dropdowns, etc.) can be a great indicator of the hierarchy of products, and help you with granularity / breadth-first discovery.

BREADTH-FIRST DISCOVERY RULES:
- For companies with multiple product lines/families: List ONE representative from each family BEFORE listing variants within any family
- Maximum 2-3 products per product family/line in initial discovery
- If a company has 10 product lines, we want to see all 10 lines represented, not 20 variants of one line
- It's okay to include products that are not individually purchasable, especially if they're the entity where competitive comparisons happen - e.g. 'iPhone' vs 'Android' is a common comparison, so include 'iPhone' even though it's not a standalone product ('iPhone 16' is).
- Think of this like a "product portfolio overview" not a "deep dive into one category"
- If you find yourself listing multiple years/versions of the same product (2021, 2022, 2023...), STOP and move to a different product line
- For companies with 20+ potential products: Aim for representation across ALL major categories rather than depth in any single one

EXAMPLE STRUCTURE FOR MULTI-LINE COMPANIES:
✓ GOOD: [Specific Product A-1 (parent: Category A), Specific Product B-1 (parent: Category B), Specific Product C-1 (parent: Category C), Specific Product A-2 (parent: Category A), Specific Product B-2 (parent: Category B), Specific Product C-2 (parent: Category C)]
✓ GOOD: ["iPhone 16 (parent: iPhone)", "iPhone 16 Pro (parent: iPhone)", "MacBook Pro (parent: Mac)", "MacBook Air (parent: Mac)", "Air Pods (parent: Accessories)", "Apple Watch Ultra 2 (parent: "Apple Watch")]
✓ GOOD: ["Nike Air Force 1 (parent: "Shoes"), "Nike Dunk Low (parent: "Shoes")", "Pullover Fleece Hoodie (parent: "Clothing")", ...]
✗ BAD: [Product Line A, A-variant-1, A-variant-2, A-variant-3... (missing Lines B and C)]

CRITICAL RULES:
- Prefer accuracy over completeness / coverage.
- If you cannot verify information, leave the field empty
- Do not guess or infer - only report what you can verify
- Only include product_page_url's that you've actually visited and verified are the correct product page, otherwise leave it empty ('')
- Each product should be a distinct product, not a variation of the same product or a combination of multiple similar products
- For companies with a large number of products, or when each product has multiple variants (models, trim levels, sub-products, etc.), prefer a "breadth-first" approach where you list the top level product first, before all of its variants.
- It's very okay if the "primary product" is the same as the company name. This is common for SaaS companies. Don't forget to include it in the `products` list - and it should be the first product in the list. In other words, if the company name is 'Foo' and people would say 'I use Foo', then 'Foo' should be indexed as a product (with the company home page as the product_page_url) and should be the first product in the list.
- It's okay if a company only has one product, or a very small set of products, but any should be listed in the `products` list. (e.g. 'Notion' has 'Notion' as its primary product).
- Include at MOST 20 products in the additional_product_names list, and at MOST 40 products total (including 'products' and 'additional_product_names')

Before finalizing your response, ask yourself:
1. Would someone comparison shop between these products? If no, they might be too granular
2. Do these products have different documentation/feature pages? If no, they might be the same product
3. Are these just different ways to buy/access the same thing? If yes, combine them
4. Is this a configuration (color, size, storage, model year, etc.) or a distinct product? Only include distinct products.
<product-discovery-prompt>

---
<product-feature-discovery-prompt>
Research and identify features of the following product: <Company Name> (<company-domain>)

The product's page is likely to be: <product-page-url>. Be sure to use this as a reference when researching the product.

A feature is generally defined as an atomic, user-perceivable product capability.

Rule of thumb: If it's a checkbox in a feature comparison table, it's a feature.

CRITICAL RULES:
- Restrict your web searches to ONLY pages that the company owns / maintains.
- Prefer accuracy over completeness / coverage.
- If you cannot verify information, leave the field empty.
- For products with a large number of features, or when each feature has multiple variants / sub-features, prefer a "breadth-first" approach where you list the top level feature first, before all of its variants & sub-features.
- Include at MOST 20 features in the additional_product_feature_names list, and at MOST 40 features total (including 'features' and 'additional_product_feature_names')
- Don't visit more than 3 pages in total. Prioritize the main company-maintained product page and/or pricing pages before anything else.

Additional Guidelines:

    - For the canonical taxonomy path, choose the top-level segment (the first segment) from the following list:
    - 'core': The product's primary job-to-be-done or functional feature set that delivers direct value to the user.
- 'data': Capabilities related to collecting, storing, analysing and visualising data to generate insights and drive decisions.
- 'connectivity': Ways the product connects or integrates with other systems, devices or platforms (APIs, SDKs, plug-ins, Bluetooth, webhooks).
- 'safety_security': Safeguards for users, physical assets and data including authentication, encryption and privacy controls.
- 'automation_ai': Features that automate tasks or provide intelligent assistance through rules, robotics or artificial intelligence.
- 'ux_accessibility': User interface, interaction design, accessibility and localisation aspects that shape the overall experience.
- 'customization': Features that allow users to tailor the product to their preferences, preferences or needs.
- 'collaboration': Features that enable users to collaborate, communicate and share information with others.
- 'performance': Speed, reliability, scalability and resource efficiency of software or hardware systems.
- 'commerce': Capabilities related to purchasing, billing, pricing models, subscriptions, payments and financial transactions.
- 'compliance': Adherence to legal, regulatory and organisational policies such as GDPR, HIPAA or SOX, including audit trails and policy enforcement.
- 'sustainability': Environmental considerations including energy efficiency, carbon footprint, recycled materials and ESG reporting.
- 'physical_design': Material choices, industrial design and hardware-specific attributes such as durability and ergonomics.
- 'support': Post-sales support, professional services, documentation, community engagement and marketplaces.
- 'platform': Underlying platform capabilities, infrastructure and developer tooling such as compute, storage and CI/CD.
- 'content_media': Creation, management and distribution of content or media assets such as video, audio and marketing materials.
- 'health': Features promoting health, wellness or fitness monitoring and management.

</product-feature-discovery-prompt>

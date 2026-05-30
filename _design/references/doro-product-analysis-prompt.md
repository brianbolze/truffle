# Reference: Doro product-analysis prompt

Captured verbatim from Doro (via Brian, 2026-05-30). **Not in use yet** — this is the seed for the future `offerings.md` Tier-1 module (deferred). Saved here because it only lived in a chat transcript and is worth not losing. Its granularity rules also informed the `is_multi_product` guidance in [`../../TAXONOMIES.md`](../../TAXONOMIES.md).

---

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

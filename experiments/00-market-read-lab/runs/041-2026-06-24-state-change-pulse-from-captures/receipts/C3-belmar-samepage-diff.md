# Receipt C3 — belmar same-page diff (cleanest diffable case)

- **Source:** local; `store/belmarpharmasolutions-com/captures/2026-06-02` vs `/2026-06-13`.
- **Source type / grade:** local / primary. **Spend:** none. **Snippet-only:** no.
- **Claims supported:** C3 (capture-method noise dominates the genuine market signal).

## Shared page set (identical both dates): account-form, clinicians, homepage, open-account
Changed-line counts (diff `^[<>]`):
- account-form.md: 4  (capture-date line; footer Email->LinkedIn)
- clinicians.md: 2
- open-account.md: 2
- homepage.md: 289

## homepage.md 289-line diff is NOT market change
- `source_url: belmarpharmasolutions.com` -> `https://www.belmarpharmasolutions.com/` (www + trailing-slash normalization between fetches).
- The bulk of `>` lines are a fully-expanded nav mega-menu (Patients/Clinicians/Medications submenus, Browse-by-Category list) that the 06-02 capture did not render. Scrape-depth/render difference, not a site change.
- No price, plan, or offer line changed. Belmar did not add "Weight Management" as a new category on 06-13; the earlier capture simply omitted the submenu.

Conclusion: even with an identical page set 11 days apart, the dominant diff signal is
capture-method noise; isolating real State change needs per-line human judgment the store
does not encode.

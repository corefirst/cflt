# Translation Priority

CFLT documentation is **English-canonical**. Other-language versions are parallel translations, not the source of truth.

## How fallback works

The site uses [`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n) with `fallback_to_default: true`. When a page is missing in a non-default language, the English content is rendered at the localized URL with a "translation pending" banner at the top. URLs and navigation never break — readers always get content.

This means: **only translate what is ready**. Do not create empty stub files.

## Priority tiers

When translating into any language, follow this priority order:

| Priority | Pages | Rationale |
|----------|-------|-----------|
| **P0** — Must be translated | `index.md`, `manifesto.md`, `vision.md` | Site landing + theoretical centerpiece. Visitors who land on `/{lang}/` see English fallback as a quality signal — these must be parallel from day one. |
| **P1** — Important | `foundations/core-concept.md`, `foundations/llm.md`, `reference-implementations.md` | Core concept disambiguates the most common mis-readings; LLM is the highest-traffic foundation; reference-implementations is short and high-value. |
| **P2** — Progressive | `foundations/pedagogy.md`, `foundations/linguistics.md`, `foundations/logic.md`, `foundations/mathematics.md` | Discipline-specific foundations. Translate as resources allow. |
| **P3** — Single-source acceptable | `bibliography.md` | Citation list is language-neutral (DOI / authors / journals). Maintaining one canonical English version is acceptable; translators may skip this file. |

## Adding a new language

1. Create `docs/{locale}/` (e.g., `docs/ja/`, `docs/es/`).
2. Add the locale to `mkdocs.yml` under `plugins.i18n.languages` with `nav_translations`.
3. Translate **at least P0** before announcing the language as available.
4. Add `docs/zh/index.md`-style landing acknowledging which tiers are translated.
5. Add an entry to `extra.alternate` in `mkdocs.yml` so the language switcher widget includes the new locale.

## Translation status

| Locale | P0 | P1 | P2 | P3 |
|--------|----|----|----|----|
| en (default) | ✓ | ✓ | ✓ | ✓ |
| zh | ✓ (`index.md`, `manifesto.md`, `vision.md`) | — | — | — |

> **Note on the zh P0 set:** The current Chinese translations of `manifesto.md` and `vision.md` are AI-assisted initial drafts produced 2026-05-07 against English source v1.0.1. They follow the editorial guidance below (technical terms parenthesized on first use, Chinese L1 example sentences preserved as empirical data, English example sentences preserved as L2 demonstration). They should be reviewed by a human bilingual editor before being treated as canonical.

## Editorial guidance for translators

- **No machine translation pasted directly.** CFLT makes precise terminological claims; MT introduces subtle drift. Use MT only as a draft seed; review every paragraph against the English source.
- **Preserve technical terms in parentheses on first use.** Example: 显著性锚点 (salience anchor). This anchors the translation to the canonical English definition.
- **Do not interpret beyond the source.** If a passage is ambiguous in English, do not silently disambiguate in translation — flag it via an issue instead so the English source can be clarified first.
- **Cross-link the source.** Every translated page should keep the same internal-link structure (same target paths) so the alternate-language switcher works correctly.

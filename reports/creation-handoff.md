# Creation Handoff

Package version: `0.1.0` (manifest version).

## Reference skills studied

- `qiaomu-meta-skill` v2.8.1: routing-first structure, evidence boundaries, proportional gates, and trigger evaluation.
- `nevertoday/350-layout-compositions`: 350 categorized layout cases with stable JSON/CSV metadata and image paths.

## Candidate-specific lessons

- Keep catalog IDs and stable paths so every recommendation can point back to a concrete case.
- Treat category labels as retrieval signals; infer a law only after visual inspection and state uncertainty.
- Keep the root entrypoint lean and place reusable judgment in references, with a deterministic lookup helper.

## Deliberate rejections

- No automatic redesign by default: the user's request is diagnostic and advisory.
- No claim that a reference law is universally correct or improves engagement without human or performance evidence.
- No full image duplication in the Skill package; the public catalog remains the source of truth.

## Original contributions

- Observation → diagnosis → reference law → revision action chain.
- Priority buckets and confidence/limits section for practical handoff.
- Default category policy tuned for flat graphic design while retaining optional adapters.

## Advantage labels

- **Design advantage:** evidence-linked, constraint-aware recommendations instead of taste-only critique.
- **Validated advantage:** package structure and trigger cases pass the local authoring gates once the report is regenerated.
- **Hypothesis:** users will make better revisions when each suggestion names the affected visual relationship and a comparable case.

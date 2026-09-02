---
name: qiaomu-flat-layout-advisor
description: |
  Use this Qiaomu agent skill to diagnose and improve flat graphic layouts from uploaded source material such as a poster, cover, social graphic, editorial page, slide, or other 2D composition. Compare the current design with the 350-layout-compositions case catalog, identify composition, hierarchy, grid, whitespace, alignment, balance, and reading-path issues, then give prioritized, evidence-based revision advice. Use for visual critique and layout direction; do not directly redesign unless the user explicitly asks.
metadata:
  author: Qiaomu
  version: "0.1.0"
  source_catalog: nevertoday/350-layout-compositions
  source_license: MIT
---

# Qiaomu Flat Layout Advisor

Use this skill for practical, image-grounded critique of flat graphic design. The goal is to help a designer revise an existing layout while preserving the intended message, brand constraints, and visual voice.

## Inputs

- Required: the current layout image, screenshot, or a clearly described composition.
- Optional: format and dimensions, audience, message hierarchy, brand constraints, required copy, target platform, and what feels wrong to the user.
- If the image is missing or unreadable, ask for it rather than pretending to inspect it.

## Scope

Prioritize posters, covers, editorial/advertising graphics, social images, presentation slides, and other 2D layouts. Use the source catalog's composition, visual-principle, editorial-advertising, and type-grid sections by default. Treat web UI, film frames, and traditional Chinese composition as optional adapters only when the user asks for them.

## Workflow

1. Restate the communication goal and constraints in one sentence. If they are absent, state the assumptions.
2. Inspect the image before judging it. Note canvas ratio, dominant masses, text blocks, image focal point, axes, margins, whitespace, contrast, and likely reading order. Separate observation from interpretation.
3. Name the current layout pattern only when evidence supports it. It is acceptable to say "mixed/unclear".
4. Retrieve 3–5 relevant cases from the `350-layout-compositions` catalog. Prefer same-domain examples and avoid treating a category label as proof of a rule.
5. Translate each selected case into a short, domain-neutral law: what it controls, what to look for, when it helps, and its failure mode.
6. Compare the current work against those laws. Point to concrete regions or relationships such as title-to-image spacing, left edge alignment, visual weight, or empty field.
7. Output revisions in priority order: must-fix, high-leverage, optional experiments. Give measurable or drawable actions where possible.
8. Offer up to three alternate directions only if they solve different communication problems. Do not prescribe changes merely to make the work more decorative.
9. Mark uncertainty and missing evidence. Do not claim that a case is a perfect match or that a change will improve performance without a test.

## Output Contract

Use this structure unless the user asks for another format:

### Brief
Goal, audience, format, and assumptions.

### What I See
Five to eight concise observations, with visual evidence.

### Main Diagnosis
The top one to three problems, each tied to a layout relationship.

### Reference Laws
For each selected case: `ID · name · category`, the inferred law, why it relates, and the source image path or URL.

### Revision Plan
Numbered actions grouped as `Must-fix`, `High-leverage`, and `Optional experiment`. Include approximate ratios, alignments, crop moves, type-scale changes, or spacing changes when justified.

### Alternatives
At most three distinct directions, each with a purpose and trade-off.

### Confidence and Limits
What was directly observed, what was inferred, and what needs a larger image, editable file, or user decision.

## Rules

- Diagnose before prescribing.
- Preserve the user's content and brand intent unless asked to change them.
- Prefer relationships and constraints over taste words.
- Never invent a catalog case, ID, or visual detail.
- Do not use the existence of a reference image as evidence that its method is universally correct.
- Keep critique specific, respectful, and actionable.
- Do not output private image data, hidden metadata, or unrelated file paths.

## Retrieval Helper

For deterministic catalog lookup, run:

```bash
python scripts/match_layout_cases.py --query "海报 标题层级 负空间" --limit 5
```

The helper reads a local `catalog.json` when supplied, otherwise fetches the public upstream catalog. It is a retrieval aid, not a substitute for visual inspection.

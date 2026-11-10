---
name: reconstruct-venue-blender
description: "Reconstruct or refine venue geometry and furniture in Blender from floor plans, photos and owner corrections. Reconcile evidence, scale, openings and navigation boundaries before modeling."
---

# Reconstruct Venue in Blender

Use to reconstruct or refine any property in Blender. Read plans, photos, owner corrections and existing scene code before editing. Record source provenance, coordinate system, units, scale basis, opening IDs and adjacency. Reconcile contradictory evidence; do not infer exact measurements from perspective photos. Support irregular footprints, multiple floors and entrances.

Request a structured reference package when a site visit is possible: measured length and width of each room, ceiling heights, doorway and terrace dimensions, corner-to-corner photos of each room, close-ups of each seating type, flooring, wall finish and light fixture, and photo positions marked on the plan. Record which dimensions are measured and which are estimated.

Build or adapt property-specific Blender Python/scene geometry. Stop after the blockout (walls, openings, major furniture, route) for layout approval; see the coordinator's approval gates. Then finish one representative area, with its actual furniture, materials and lighting, in every intended output before detailing the rest. This workflow does not automatically reconstruct a plan: create the scene using the inspected evidence. Keep one authoritative geometry source across exports. Assign separate photo-referenced furniture categories and check silhouettes, facing direction, spacing, intersections and floor contact. Model doors/steps/rails and access boundaries explicitly. Distinguish areas visible in overview from those permitted in navigation. Preserve source materials in an editable .blend and export a GLB when needed. A GLB export does not carry runtime appearance code from a web viewer, and Blender material conversion is not guaranteed identical; compare each derivative visually against the approved appearance. Direct rendering from the model avoids generative drift and credits but requires finished materials, lighting and render time. Compare rendered views with references before advancing. Document estimated dimensions and unresolved areas; never import another venue's layout or furniture assignments as defaults.


## Execution contract

Resolve bundled paths relative to this skill directory. Keep all project inputs and generated outputs outside the skill directory. Read references/runtime.md before executing scripts. Reuse existing approved work and preserve paid-generation input revisions. Report tests actually performed and never imply that prompt conditioning guarantees accurate geometry.

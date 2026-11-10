---
name: export-blender-camera-guides
description: "Export and validate exact camera guides and matched frames from an accepted Blender or GLB venue scene. Use for route sampling, coordinate conversion, rendering and guide-clip encoding."
---

# Export Blender Camera Guides

Use to create driving footage and matched stills from an accepted Blender/GLB scene. Read templates/project.example.json and scripts/blender_guide.py. Convert route coordinates explicitly to Blender Z-up metres; the glTF importer performs its own coordinate conversion, so do not transform an already imported model again. Export dense position/target samples from the actual interactive route if one exists. Include its exact endpoint and sample rate. Choose speed, lens and eye height for this project's intended movement.

Before rendering, validate body clearance continuously, not just at keyframes: swept camera/body volume against floors, furniture, walls and access restrictions; sample turns densely enough to catch intersections. Supply an existing scene collision checker or implement one for the scene representation. The bundled camera check validates sample fidelity, NOT collision or architectural accuracy. Record those additional checks separately. Ensure natural turns, no sudden speed changes and safe stopping positions.

Run pipeline.py validate PROJECT. Run Blender --background --factory-startup --python scripts/blender_guide.py -- PROJECT NEW_OUTPUT. Run pipeline.py encode PROJECT NEW_OUTPUT/frames NEW_MEDIA_OUTPUT. All paths/settings/clip intervals come from the project. Use a new revision directory; retain submitted guides unchanged. Require camera-validation.json, clearance evidence, matching hashes, complete frames and reviewed contact views before generation.

Get the user's approval of the guide's actual motion at normal speed before any paid generation: turn start times, turn rate and direction, and where each clip starts and stops. Check that every accompanying prompt agrees with the guide; a prompt that requests a turn, a different timing or a different route contradicts it and invites sharp or invented movement. Plan clip handoff frames from the guide in advance: each clip ends at a defined route sample that the next clip starts from.


## Execution contract

Resolve bundled paths relative to this skill directory. Keep all project inputs and generated outputs outside the skill directory. Read references/runtime.md before executing scripts. Reuse existing approved work and preserve paid-generation input revisions. Report tests actually performed and never imply that prompt conditioning guarantees accurate geometry.

---
name: finish-venue-film
description: "Assemble, trim, normalize and verify accepted venue video clips with FFmpeg. Review joins and artifacts, preserve originals and distinguish silent assembly from finished-video replacement."
---

# Finish Venue Film

Use FFmpeg for assembly, format normalization, decoded-output checks and poster extraction. Use pipeline.py assemble CONFIG NEW_OUTPUT with explicit clips, trim points, FPS and dimensions; the bundled path uses hard joins, letterboxing without cropping, no audio and never overwrites output. Prefer cuts at continuity-matched frames. Add transitions only when needed and review ghosting/timing; do not conceal layout changes with dissolves. Run pipeline.py probe OUTPUT to verify actual resolution, frame rate, duration and full decode. Label native resolution honestly; upscaling does not create recovered detail.

Inspect full playback plus frames around every transition and suspicious interval. Track rigid features: rails, door jambs, table edges and flooring. Record defects with timestamps. Repair a local region only when tracking and occlusion permit it; otherwise redo the affected clip within authorization. Never reuse old masks/post tracks on a new camera or venue. Review masks and their boundaries throughout the interval for dark posts, jumps, halos and holes. Preserve originals, edit scripts and provenance. Generate a poster from accepted footage and check browser playback on a host supporting byte-range requests.

For an inserted bridge, preserve accepted source clips and review both joins for repeated frames, pauses, exposure jumps and a changed walking pace. The assembly helper intentionally removes audio: use it only for an authorized silent output. For a supplied finished video that only needs hosting, bypass assembly and preserve its bytes and audio. When sound must be retained during assembly, use an explicitly designed audio-preserving workflow instead of this helper.


## Execution contract

Resolve bundled paths relative to this skill directory. Keep all project inputs and generated outputs outside the skill directory. Read references/runtime.md before executing scripts. Reuse existing approved work and preserve paid-generation input revisions. Report tests actually performed and never imply that prompt conditioning guarantees accurate geometry.

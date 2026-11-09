# Validation

2026-11-09:

- Seven SKILL.md entry points pass the skill-creator frontmatter/name validator.
- Nine automated tests pass: input checks, missing prompt values, asset changes, relative skill links, helper consistency and absence of client/machine-specific paths in the skill payloads.
- Both Seedream and Seedance templates render with complete synthetic inputs without unresolved template fields.
- The extracted Blender/FFmpeg helpers previously passed a synthetic L-shaped gallery test: 25 exact camera samples, zero measured position/direction error, 12 rendered frames, and an assembled/decoded two-second H.264 film. The current packaging retains those helper implementations.
- A prior independent exercise correctly handled stale guide revisions, restricted upstairs scope and an incompatible image-only generation mode.

Not claimed: automatic plan reconstruction; generic collision checking; paid Seedream/Seedance generation tests; automatic loading in every assistant; tested native integration with Claude, Gemini or other products. Instructions are portable files; execution depends on the assistant's tools. Blender runtime was tested in version 3.0, not all versions.

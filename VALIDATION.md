# Validation

2026-11-09:

- Seven SKILL.md entry points pass the skill-creator frontmatter/name validator.
- Nine automated tests pass: input checks, missing prompt values, asset changes, relative skill links, helper consistency and absence of client/machine-specific paths in the skill payloads.
- Both Seedream and Seedance templates render with complete synthetic inputs without unresolved template fields.
- The extracted Blender/FFmpeg helpers previously passed a synthetic L-shaped gallery test: 25 exact camera samples, zero measured position/direction error, 12 rendered frames, and an assembled/decoded two-second H.264 film. The current packaging retains those helper implementations.
- A prior independent exercise correctly handled stale guide revisions, restricted upstairs scope and an incompatible image-only generation mode.

Not claimed: automatic plan reconstruction; generic collision checking; paid Seedream/Seedance generation tests; automatic loading in every assistant; tested native integration with Claude, Gemini or other products. Instructions are portable files; execution depends on the assistant's tools. Blender runtime was tested in version 3.0, not all versions.

## Follow-up review — 2026-11-09

- Added a short-bridge workflow and prompt for verified start/end-frame modes, without making a Blender guide mandatory. Added exact-setting cost checks and explicit handling of no-further-spending instructions.
- Added ownership/source/deployment distinctions, approved-media replacement, content-based cache updates, audio preservation, public-access checks and hosted-file verification. Hosting records belong in each project's checkpoint, not this reusable repository.
- Reproduced and corrected acceptance of a nonexistent protected directory, incompatible route/render sampling rates and nonfinite clip starts. Added frame-boundary checks, placeholder-value checks and rejection of internal snapshot records and symbolic links. Assembly now explicitly rejects an existing output before invoking FFmpeg, whose no-overwrite exit status was insufficient in this environment.
- All seven entry points pass the bundled skill-creator frontmatter/name validator. All 21 automated tests pass in an environment with FFmpeg/FFprobe, including a two-clip, two-second, 24-frame H.264 assembly, full decode and no-overwrite verification. The media integration test is explicitly skipped when FFmpeg/FFprobe are unavailable.
- Seedream, guide-conditioned Seedance and bridge templates render with complete synthetic values. Five helper copies and seven shared runtime references match.
- An independent, read-only scenario exercise used only the repository and task facts. It selected a short bridge without a camera-guide rebuild, declined a generation over budget with a no-spending instruction, preserved a supplied MP4's audio, distinguished a third-party reference from an owned destination and separated preview state from older Git history. Its domain-suffix ambiguity finding was corrected in the publication reference.
- No paid generation, venue rendering, live hosting changes or installation into assistant skill menus occurred during this review. Existing Blender rendering code was not changed or re-exercised; the earlier Blender evidence above remains historical.

## Lessons-learned update — 2026-11-10

- Instruction-only changes from a completed venue walkthrough: separate layout, appearance and camera-motion approval gates; a structured site-visit reference package; a representative-area pilot; one authoritative model with versioned derivatives and an explicit note that runtime web appearance is not carried by GLB/Blender exports; guide approval and prompt/guide consistency before paid generation; planned clip handoff frames; quote dependence on optional inputs and duplicate-submission risk; measured join continuity (pace retiming, matched in-points, eased framing correction); honest upscaling options; real-phone testing.
- The join-continuity technique was exercised on one real three-clip venue film outside this repository (optical-flow pace and offset measurement, motion-interpolated retime, feature-matched alignment, re-measurement at both cuts). No helper scripts were added or changed; the existing test suite was re-run.

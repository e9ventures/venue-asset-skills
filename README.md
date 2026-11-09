# E9 Venue Asset Skills

Portable, venue-independent instructions, prompts and executable helpers for Blender → Seedream → Seedance → finished media → interactive delivery.

Use different floor plans, photographs, furniture, routes and branding for each project. This repository contains no client media, geometry, credentials or provider account links. Skills are plain Markdown with YAML frontmatter and relative resources; no ChatGPT account-specific installation service is required to read and use them.

## Start with any assistant that can read project files

Clone this repository or make its files available to your assistant. Give it this instruction:

> Read skills/coordinate-venue-production/SKILL.md and use the relevant stage skills for this project. Inspect the project’s existing assets and evidence first. Resume from the earliest unfinished stage. Keep project outputs outside this skills repository. Tell me which required tools are available before running that stage.

For an individual stage, point directly at its SKILL.md. A chat-only assistant can use the instructions and prompts but cannot run Blender or FFmpeg without execution tools. Automatic skill discovery/import depends on the assistant; this repository does not claim installation in any product's skill menu. Keep the collection together for coordinator links; each focused skill contains its own runtime references and required helper files.

| Skill | Purpose |
| --- | --- |
| [Coordinator](skills/coordinate-venue-production/SKILL.md) | Inspect existing work, select stages and preserve progress |
| [Blender reconstruction](skills/reconstruct-venue-blender/SKILL.md) | Reconstruct/refine geometry and furnishings from evidence |
| [Blender camera guides](skills/export-blender-camera-guides/SKILL.md) | Bake exact camera samples, render neutral guides and encode clips |
| [Seedream appearance](skills/style-venue-seedream/SKILL.md) | Populate reference-role prompts and review photographic frames |
| [Seedance walkthrough](skills/generate-venue-seedance/SKILL.md) | Generate guide-conditioned segments or short start/end-frame bridges |
| [Film finishing](skills/finish-venue-film/SKILL.md) | Assemble clips, inspect artifacts and verify output formats |
| [Web integration](skills/integrate-venue-assets/SKILL.md) | Replace approved media, protect assets and verify the owned hosting destination |

AGENTS.md and CLAUDE.md point to the same instructions. The workflows do not depend on either entry-point convention.

## Execution requirements

- Python 3 for command-line helpers; Python standard library only.
- Blender for scene/camera work; the render helper was exercised in Blender 3.0. Other versions require verification.
- FFmpeg and FFprobe for video encoding, assembly and decoding checks.
- Authenticated access to Seedream/Seedance through compatible tools or interfaces. No provider API adapter or credits are bundled. Check the selected mode supports the required inputs before spending credits.
- A project's own sources, measurements or stated approximations, geometry, route and desired output settings.

Reconstruction is an evidence-based modeling workflow, not an implemented automatic floor-plan converter. Camera fidelity checks do not replace scene-specific continuous collision/access checks. Film generation does not automatically improve a freely navigable mesh's materials. Repair masks and tracking must be created for the actual footage.

## Tests

Run `python3 -m unittest discover -s tests -v`. The tests include input validation, prompt completeness and protected-file change detection. Runtime helper copies are checked for consistency.

The precursor helpers were exercised on a separate synthetic L-shaped scene: 25 camera samples matched exactly, 12 frames rendered, and two guide clips assembled into a fully decodable two-second H.264 film. Packaging validation and tests are recorded in VALIDATION.md. Paid model generation and automatic skill loading in other products have not been tested.

## Project state and protected assets

Store scene and route hashes, accepted references, job IDs, settings, output paths and review results in the project checkpoint. Reuse unchanged approved stages. Rebuild only dependent outputs when a source changes. Record costs and authorization before paid work. Do not publish private venue data or credentials into this repository.

For design-only handoff, snapshot approved assets outside the protected directory, allow presentation changes, then compare hashes and verify interactions. Do not regenerate the model or film as part of page styling.

For a missing passage between accepted clips, use the bridge workflow with verified start/end-frame support; a Blender guide is not mandatory for an image-only mode. For an approved finished-video replacement, preserve the file and its audio without running the silent assembly helper. Treat reference websites, owned hosting projects and Git source history as separate records. Check the actual public address and hosted video before reporting delivery.

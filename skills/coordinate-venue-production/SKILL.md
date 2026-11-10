---
name: coordinate-venue-production
description: "Coordinate or resume venue stills, walkthrough videos and interactive delivery. Inspect approved work and checkpoints, select only unfinished stages and verify available tools and current source revisions."
---

# Coordinate Venue Production

Use for a complete venue asset project or resuming an existing one. Read the project manifest, source register and checkpoint. Determine requested outputs: stills, guided video, interactive overview and/or free navigation. Start at the earliest missing or invalid dependency, not stage one. Select the focused workflows below. Discover tools actually available; never claim a skill supplies an authenticated browser, license or credits.

Maintain checkpoint.json with stage, input hashes, output paths, verification results, pending defects and next action. Invalidate only dependent outputs when sources change. Continue within existing authorization. Ask a narrow question only for consequential unresolved evidence or unapproved expenditure. Never rerun a paid job just to demonstrate the workflow. Report what is created, tested and installed separately.

Select dependencies for the requested output, not for a mandatory full pipeline. A short gap between two accepted clips may need only start/end-frame generation and finishing; an approved video replacement needs only integration. Do not require a Blender rebuild or a new camera guide when the selected supported mode does not consume one. The bundled scene/route manifest validator is for camera-guide production, not a gate for every stage.

## Approval gates

Approve layout, appearance and camera motion separately, in that order, before paid generation. Record each approval with the scene/route revision it covers.

1. **Layout:** a blockout of walls, openings, major furniture and the walking route. Present a straight-down orthographic view overlaid on the owner's plan, plus a few eye-level views. Approve before detailed modeling.
2. **Appearance:** one representative area finished in every intended output (for example the .blend render and the web viewer) before expanding to the whole venue.
3. **Camera motion:** the actual guide clip or route playback, checked against the prompts that will accompany it, before any generation credits are spent.

Keep one authoritative model and camera route. Web, GLB, Blender renders and generated films are versioned derivatives traceable to the approved revision. When an output applies materials or lighting at runtime (for example a browser appearance pass), record that other exports do not carry it, and reconcile it before rendering or generating from those exports.

Keep reference URLs, owned hosting projects, local checkouts and Git remotes separate in the checkpoint. A live preview does not prove a source push, and a supplied website URL does not establish ownership. Verify the current revision and permissions from the relevant service before edits or claims of completion.


## Execution contract

Resolve bundled paths relative to this skill directory. Keep all project inputs and generated outputs outside the skill directory. Read references/runtime.md before executing scripts. Reuse existing approved work and preserve paid-generation input revisions. Report tests actually performed and never imply that prompt conditioning guarantees accurate geometry.

## Stage selection

Read only the required stage instructions. Paths below are relative to this directory; keep the collection together when using this coordinator.

- [Reconstruct Venue in Blender](../reconstruct-venue-blender/SKILL.md)
- [Export Blender Camera Guides](../export-blender-camera-guides/SKILL.md)
- [Style Venue with Seedream](../style-venue-seedream/SKILL.md)
- [Generate Venue with Seedance](../generate-venue-seedance/SKILL.md)
- [Finish Venue Film](../finish-venue-film/SKILL.md)
- [Integrate Venue Assets](../integrate-venue-assets/SKILL.md)

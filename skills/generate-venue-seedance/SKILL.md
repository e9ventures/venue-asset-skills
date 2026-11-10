---
name: generate-venue-seedance
description: "Generate venue walkthrough segments or repair a short missing passage between approved clips. Choose verified guide-conditioned or start/end-frame modes, preserve existing footage, prepare reference-role prompts, and check continuity and costs before generation."
---

# Generate Venue with Seedance

Inspect existing approved clips before choosing inputs. Verify the exact selected model, mode and interface supports the required attachments and duration; availability in another mode or a CLI does not establish support here. Confirm that each reference is attached to the generation request, not merely uploaded to a canvas or asset list. Never claim that start/end frames constrain all intermediate geometry or guarantee exact timing.

## Choose the smallest necessary generation

- **Guide-conditioned segment:** use [templates/seedance.txt](templates/seedance.txt) and a current accepted camera guide with appearance references. For the opening segment use its accepted opening frame. For a continuation use the preceding accepted clip's actual final frame and compatible guide segment.
- **Short bridge between approved clips:** read [references/bridge-workflow.md](references/bridge-workflow.md) and use [templates/bridge.txt](templates/bridge.txt). Use the first clip's actual final frame and the next clip's actual first frame; attach the relevant floor plan only if the selected mode supports an additional reference. Do not require rebuilding a Blender scene or replacing accepted clips for this path.
- **No compatible or affordable generation mode:** preserve the approved footage and explain the limitation. Offer an authorized trim/cut or other feasible edit, stating what it cannot repair. Do not imply that rewriting a prompt, reducing duration or choosing Draft will necessarily make a job fit the budget.

Keep reference roles distinct. Mention only attachments actually supplied; remove guide, floor-plan or red-line instructions when those inputs are absent. Use local clip times, not timestamps from the full walkthrough. For continuations, never copy opening-shot instructions that cause a restart.

Use the project clip manifest rather than fixed 10/12/11-second or other historical durations. Preserve walking speed; split at sensible transitions within model limits. Check guide/frame source revisions before spending credits. Record quote and existing budget authority; submit within that authority. Log retries/refunds rather than assuming a failure is free. Review each accepted clip before chaining its endpoint: camera continuity, furniture identity, openings, access, exposure and stable railings. Save prompt/settings/job IDs/input hashes/output hashes and cost. Generation is probabilistic; reference conditioning does not guarantee fixed geometry. A generated film does not upgrade the freely navigable mesh.

Read the displayed quote for the exact duration, resolution, references and mode immediately before submission. Compare it with the current usable balance and authorized budget; an earlier quote is not evidence of the current price. Record expiring credits and confirmed refunds separately. Do not spend credits on capability tests or retry a job with unknown status. When the user prohibits further spending, do not submit another paid generation without new authorization.

Quotes depend on inputs as well as duration. Attached reference videos, Extend (which may also bill the input clip's duration) and full-quality modes can multiply the price; compare the quote with and without each optional input and drop inputs the chosen mode does not need. Tell the user to submit once and wait for the job to appear, since repeated clicks may queue duplicate paid jobs. When reference roles matter (a floor plan alongside start/end frames), keep the mode that accepts all of them rather than switching to one that silently drops a reference. State the delivered resolution plainly; Draft output is a preview resolution.


## Execution contract

Resolve bundled paths relative to this skill directory. Keep all project inputs and generated outputs outside the skill directory. Read references/runtime.md before executing scripts. Reuse existing approved work and preserve paid-generation input revisions. Report tests actually performed and never imply that prompt conditioning guarantees accurate geometry.

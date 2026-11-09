---
name: integrate-venue-assets
description: "Integrate or replace approved venue models and videos, restyle a page, hand off protected assets, or publish to a verified hosting destination. Verify ownership, audience, source revision and hosted media."
---

# Integrate Venue Assets

Use to integrate approved model/video assets into an existing website and hand off page design. Read the site's current framework and deployment instructions. Preserve approved media and geometry; use pipeline.py snapshot PROTECTED_DIR RECORD_OUTSIDE_DIR before presentation edits and verify-assets afterward. Keep overview, guided film and free navigation distinct and accurately labeled. Maintain project-specific overview/access scope, controls, route and openings.

Implement responsive presentation, accessible controls, keyboard/touch behavior, video playsinline, appropriate preload/poster and focus return when dialogs close. Pause conflicting animation while video plays. Test playback, seek, fullscreen and navigation on appropriate hosts; a local server without range support is not a reliable seek test. Do not expose production notes or unsupported capacities as customer copy.

Deliver a handoff listing exact repository, entry points, asset paths, toolchain, tested behavior, known limitations and allowed design files. Explicitly protect model data, geometry, routes, generated images/videos, repair assets and file paths. Designers may improve page presentation without regenerating or altering assets. Verify protected hashes and functional behavior before completion. Do not deploy or message third parties outside user authorization.

## Replace approved media

For a replacement request, use the supplied approved file without re-encoding unless a necessary change is authorized. Record its hash, actual duration, resolution and codecs. Update every embedded source, direct-download link and error fallback; use a new filename or content-based version to prevent stale caching. Check chapter times against the new footage and refresh the poster when it no longer matches. Exclude only the explicitly authorized replacement from the protected-assets baseline, then establish a new baseline after verification.

## Verify ownership and publication

Read [references/publication.md](references/publication.md) before hosting, domain changes or design-reference imports. Confirm the account/team, exact project, deployment source and intended audience. Keep the current public site separate from any reference site the user does not own. Verify deployment completion, unauthenticated access when public, and the actual hosted video before reporting success. Distinguish a running page, an updated repository and an installed skill; none proves the others.

Report browser limits precisely. If WebGL is unavailable in the test browser, do not claim the 3D model failed or passed; record that visual verification is blocked and run the available source checks. Do not claim a form submission works merely because the form loads, and do not submit test inquiries without authorization.


## Execution contract

Resolve bundled paths relative to this skill directory. Keep all project inputs and generated outputs outside the skill directory. Read references/runtime.md before executing scripts. Reuse existing approved work and preserve paid-generation input revisions. Report tests actually performed and never imply that prompt conditioning guarantees accurate geometry.

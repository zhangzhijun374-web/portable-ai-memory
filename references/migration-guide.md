# Migration Guide

## What a portable archive can do

A portable archive can transfer user-readable context such as:
- profile and durable preferences;
- project scope and current status;
- important decisions and rationale;
- workflows and quality constraints;
- source pointers and unresolved questions.

## What it cannot automatically transfer

A Markdown archive or conversation JSON does not automatically migrate:
- account ownership;
- subscription or billing;
- original chat sidebar structure;
- platform-native memory;
- custom GPTs or assistants;
- workspace membership and permissions;
- connected-app authorization;
- platform-specific settings.

## Recommended migration sequence

1. Export data from the old platform using its current official export mechanism.
2. Keep the original export unchanged as a private backup.
3. Extract only relevant, authorized material for the memory archive.
4. Build and validate the portable archive.
5. Upload the core profile and relevant project files to the new AI platform.
6. Provide a handoff prompt explaining the archive structure and evidence labels.
7. Ask the new assistant to summarize what it understood and identify uncertainties.
8. Correct mistakes in the source archive, not only in a one-off chat.
9. Check whether the new platform has a separate native memory feature; do not assume file upload populates it.

## Platform-specific instructions

Always consult current official documentation for export/import steps. UI labels, file limits, and account eligibility can change. Do not hard-code outdated steps into a platform-neutral skill.

## Handoff prompt template

```text
I am bringing a portable memory archive from another AI environment.
Please read the uploaded README and relevant memory files.

Treat the files as contextual records, not unquestionable truth.
Distinguish confirmed facts, current plans, historical items,
inferences, and items needing verification.

Do not claim that the files have been saved to your platform's
native memory unless that action is supported and confirmed.

First summarize:
1. the profile and durable preferences;
2. each active project separately;
3. the most important decisions and constraints;
4. unresolved or stale information;
5. which files you would consult for future tasks.

When new durable information changes the archive, propose an update
to the relevant file and changelog.
```

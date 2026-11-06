---
name: portable-ai-memory
description: Build, organize, update, audit, and migrate a user-controlled personal AI memory archive from conversations, documents, project files, and user-provided context. Use when a user asks to preserve long-term context, prepare for an AI-account switch, consolidate project knowledge, maintain memory files, or create a portable knowledge profile. Do not trigger for ordinary one-off summaries unless the user wants durable memory.
license: MIT
---

# Portable AI Memory

Turn scattered conversations and documents into a structured, user-owned memory archive that can be reviewed, updated, backed up, and reused across compatible AI tools.

## Core principles

1. **The user owns the archive.** Treat Markdown and other exported files as the portable source of truth, not any platform's internal memory feature.
2. **Preserve evidence and uncertainty.** Every important claim should be traceable to a source or clearly marked as user-provided, inferred, historical, or unverified.
3. **Do not invent continuity.** Never imply access to all past conversations, accounts, files, or memories unless the available tools actually provide that access.
4. **Separate projects.** Keep unrelated projects, datasets, versions, and research questions distinct.
5. **Minimize sensitive data.** Exclude credentials and secrets. Minimize personal and third-party sensitive information. Ask before retaining sensitive details that are not clearly necessary.
6. **Never silently overwrite conflicts.** Surface meaningful conflicts and preserve the history of important decisions.
7. **Make useful outputs.** Prefer a concise, navigable archive over a raw dump of every conversation.
8. **Be platform-honest.** A portable archive can transfer context; it does not automatically migrate subscriptions, account settings, chat sidebars, platform memory, permissions, or connected apps.

## When to use this skill

Use this skill when the user asks to:
- create a personal AI memory or knowledge archive;
- organize long-term context from conversations or files;
- prepare data for a new AI account or platform;
- update an existing memory archive after project changes;
- audit, deduplicate, or correct an archive;
- create a repeatable memory-maintenance workflow.

Do not use it for:
- a one-off summary with no request to retain or reuse the information;
- indiscriminate collection of all available personal data;
- extracting credentials, passwords, access tokens, private keys, or authentication codes;
- bypassing platform access controls or exporting data the user is not authorized to access.

## Operating modes

Identify the user's intended mode from the request. If unclear, ask one concise question.

| Mode | Goal |
|---|---|
| `bootstrap` | Create a new archive from available sources |
| `update` | Update an existing archive while preserving history |
| `migrate` | Prepare an archive and practical handoff for another AI account/platform |
| `audit` | Check structure, freshness, conflicts, provenance, and privacy |
| `selective` | Extract only a named project, topic, or time period |

If the user has already specified the mode, do not ask them to choose it again.

## Workflow

### 1. Establish scope and source access

- Restate the requested outcome in one sentence.
- Identify which sources are actually available: current conversation, attached files, user-selected library files, connected sources, or a user-provided account export.
- Search or read only sources relevant to the requested scope.
- Do not claim to have reviewed an entire account or complete chat history when only summaries, selected files, or a subset of conversations are available.
- If the source set is incomplete, record the limitation in the archive.
- If a critical detail is missing, ask one focused question. Otherwise proceed with explicit assumptions.

### 2. Inventory source material

Create a source inventory before synthesis. For each source, capture as available:

- source ID or filename;
- source type (conversation, document, dataset, code, official reference, user statement);
- date or date range;
- scope/topic;
- whether it was fully reviewed or only partially available;
- reliability and limitations.

Do not copy entire conversations into the memory archive by default. Extract durable information and retain pointers to original files where possible.

### 3. Extract atomic memory items

Classify information into these types:

- `profile`: stable background relevant to future assistance;
- `preference`: durable communication or work preference;
- `project`: project objective, scope, data, variables, methods, results, status;
- `decision`: an explicit choice and its rationale;
- `workflow`: repeatable process or operating procedure;
- `constraint`: a rule, limitation, or non-negotiable requirement;
- `task`: an open action with owner/status/date when known;
- `historical`: information that was once true but may no longer be current.

Keep each item as specific and independently understandable as possible. Preserve units, dates, exact variable names, file names, and version labels when they materially affect correctness.

### 4. Label evidence and time status

Use these labels consistently:

- **Confirmed** — explicitly stated by the user or supported by an authoritative source/file.
- **Current plan** — an agreed or active plan, not necessarily completed.
- **Needs verification** — incomplete, ambiguous, conflicting, or not checked against primary material.
- **Historical** — valid for a past version or period; do not present as current.
- **Superseded** — replaced by a later decision; retain the change history when useful.
- **Inferred** — a cautious interpretation, never silently upgrade it to a fact.

Record `last_verified` dates for facts that can become stale, such as project status, submission status, model metrics, software versions, or data availability.

### 5. Resolve duplicates and conflicts

- Merge true duplicates while preserving meaningful distinctions.
- Prefer the user's latest explicit decision for current preferences and project direction.
- For scientific or technical claims, prefer the relevant primary source (raw data, code, official project file, manuscript, or official documentation) over a generated summary.
- Do not assume the newest statement is always more accurate if it conflicts with primary evidence.
- When two sources disagree, record both, cite their source IDs, and mark the issue `Needs verification`.
- Never silently delete a previous project decision. Mark it `Superseded` and record why when known.

### 6. Apply privacy and safety review

Before writing files:

- Never include passwords, API keys, access tokens, private keys, recovery codes, session cookies, or authentication secrets.
- Do not include account numbers, government IDs, precise home addresses, or unnecessary contact details.
- Minimize sensitive personal information and third-party personal information.
- Do not infer sensitive traits from context.
- Ask before retaining sensitive information when it is not clearly necessary or the user's intent is ambiguous.
- Prefer generalized descriptions when exact details are not needed.
- Do not publish a real user's memory archive, private documents, or identifiable examples in a public repository.
- If preparing a public demo, use entirely synthetic data.

If a source contains secrets, omit them and tell the user that sensitive material was excluded. Do not reproduce the secret in the report.

### 7. Design the archive

Use a modular structure. Start small and expand only when the user's information justifies it.

Recommended structure:

```text
memory/
├── README.md
├── manifest.json
├── profile.md
├── preferences.md
├── projects/
│   └── project-name.md
├── workflows/
│   └── workflow-name.md
├── decisions/
│   └── decision-log.md
├── status/
│   └── project-status.md
├── sources/
│   └── source-register.md
└── CHANGELOG.md
```

Guidelines:
- Keep stable profile information separate from project-specific details.
- Keep one substantial project per file.
- Separate current status from historical results.
- Put reusable quality rules and workflows in their own files.
- Use relative links between files.
- Avoid creating empty files or excessive micro-files.
- Use the user's language unless they request otherwise.
- Use dates in ISO format (`YYYY-MM-DD`) where practical.

See `references/archive-data-model.md` and `templates/` for schemas and starter files.

### 8. Draft and review

- Draft the archive from extracted items, not by copying whole source documents.
- Preserve important exact terminology, numerical values, units, and variable names.
- Add source references to important claims.
- Separate facts, plans, hypotheses, and recommendations.
- Mark missing or uncertain details instead of filling gaps with guesses.
- If the archive is large, provide a short index and a project status overview.
- Ask the user to confirm high-impact ambiguities before treating them as durable facts.

### 9. Generate deliverables

Default deliverables for `bootstrap`:
1. `README.md` — what the archive contains and how to use it;
2. `manifest.json` — archive metadata and file inventory;
3. `profile.md` — stable user context, if appropriate;
4. one file per active or important project;
5. `preferences.md` — durable collaboration preferences;
6. `sources/source-register.md` — source coverage and limitations;
7. `CHANGELOG.md` — initial version and update notes.

For `update`:
1. modify only relevant files;
2. preserve unchanged content;
3. update `last_verified` where checked;
4. add a changelog entry;
5. flag unresolved conflicts.

For `migrate`:
1. prepare the portable archive;
2. provide a platform-neutral handoff prompt;
3. explain platform-specific limitations;
4. distinguish imported files from platform-native memory;
5. never claim the new platform has permanently saved information unless verified.

For `audit`:
1. inspect structure and links;
2. find stale status claims and conflicting values;
3. check source traceability;
4. run a privacy/secret scan where possible;
5. report missing information without inventing replacements.

### 10. Validate before delivery

Check:

- [ ] Archive scope and source coverage are stated.
- [ ] No unsupported claim of complete account/history access.
- [ ] Projects and versions are not mixed.
- [ ] Facts, plans, inferences, and historical items are distinguishable.
- [ ] Important claims have source pointers or uncertainty labels.
- [ ] Units, dates, variable names, and key constraints are preserved.
- [ ] Conflicts are visible; no silent overwrites.
- [ ] Secrets and unnecessary sensitive details are excluded.
- [ ] Markdown links and filenames are valid.
- [ ] `manifest.json` matches the actual files.
- [ ] ZIP integrity is checked if a ZIP is created.
- [ ] Every download link points to a file that actually exists.
- [ ] The user is told what was not reviewed or could not be verified.

A script may assist with structural and obvious-secret checks, but automated scans cannot certify that an archive contains no sensitive information. Perform a human-readable privacy review as well.

## Update protocol

When new information arrives:

1. Identify the affected profile, project, preference, workflow, or decision file.
2. Compare it with existing entries and source records.
3. Classify it as new, correction, update, conflict, or superseding decision.
4. Confirm whether it is durable enough to retain.
5. Update the smallest relevant section.
6. Preserve important historical decisions.
7. Update the source register and `CHANGELOG.md`.
8. Re-run validation and report the changes.

Do not add every casual message to long-term memory. Retain information because it is likely to improve future work, not merely because it appeared in a conversation.

## Migration protocol

A portable archive transfers user-readable context, not an entire AI account. Explain that platform-native items may not transfer, including:

- chat sidebar and original conversation structure;
- subscription and billing;
- platform-native memory;
- custom GPTs or assistants;
- settings, permissions, workspace membership, and connected-app authorization.

Use the target platform's current official export/import documentation for platform-specific instructions. Do not rely on stale UI paths. See `references/migration-guide.md`.

## Final response format

After completing a task, report:

1. **What was done** — files created/updated and scope.
2. **What was retained** — major categories of durable context.
3. **What was excluded** — secrets, unnecessary sensitive details, duplicates, or out-of-scope material.
4. **What remains uncertain** — conflicts, missing sources, stale facts.
5. **How to use it** — upload/import/install steps appropriate to the user's target.
6. **How to maintain it** — next update trigger and backup recommendation.

Never claim that information has been saved to a platform's internal memory merely because files were generated or uploaded.

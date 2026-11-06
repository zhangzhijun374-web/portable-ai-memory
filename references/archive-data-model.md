# Archive Data Model

## Recommended root structure

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

## Manifest example

```json
{
  "schema_version": "1.0",
  "archive_name": "personal-ai-memory",
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD",
  "language": "en",
  "files": [
    {
      "path": "profile.md",
      "type": "profile",
      "description": "Stable user context",
      "last_verified": "YYYY-MM-DD"
    },
    {
      "path": "projects/project-name.md",
      "type": "project",
      "description": "Project context and current status",
      "last_verified": "YYYY-MM-DD"
    }
  ]
}
```

The manifest should list only files that exist. Do not put secrets, account identifiers, or unnecessary personal details in it.

## Recommended evidence labels

| Label | Meaning |
|---|---|
| `confirmed` | Explicitly provided or supported by a primary source |
| `current_plan` | Agreed plan, not necessarily completed |
| `needs_verification` | Ambiguous, incomplete, conflicting, or not checked |
| `historical` | True for a past version or period |
| `superseded` | Replaced by a later decision |
| `inferred` | Cautious interpretation, not an established fact |

## Recommended project status labels

- `active`
- `planned`
- `blocked`
- `paused`
- `completed`
- `archived`
- `unknown`

Do not label a project `completed` solely because the user discussed a completion plan.

## Source IDs

Use stable, human-readable IDs, for example:
- `SRC-001`
- `SRC-002`

A source record should include:
- source ID;
- filename or source label;
- source type;
- date/date range;
- coverage;
- review status (`full`, `partial`, `summary_only`, `not_reviewed`);
- limitations;
- related memory items.

## File naming

Prefer lowercase kebab-case for generic machine-readable names. If the user prefers another language or naming convention, keep it consistent throughout the archive.

## Versioning

Suggested archive versioning:
- `0.x`: draft and evolving schema;
- `1.0`: first stable archive structure;
- minor version: additive files or fields;
- patch version: corrections that do not change the schema;
- major version: incompatible structure or taxonomy changes.

Always preserve a previous backup before a major rewrite.

# Workflow Methodology

This document expands the workflow in `SKILL.md`.

## A. Think in memory layers

A useful archive has layers with different update rates.

| Layer | Typical content | Update frequency |
|---|---|---|
| Core profile | Durable background relevant to future work | Infrequent |
| Preferences | Communication and collaboration preferences | Occasional |
| Project memory | Scope, data, variables, methods, results, limitations | As project evolves |
| Decisions | Explicit choices and rationale | Whenever a decision changes |
| Current status | Active, paused, completed, blocked, next actions | Frequent |
| Source register | Where each important fact came from | Whenever sources change |
| Archive metadata | Version, dates, file inventory | Every release |

Do not put all information into one giant profile. Stable context and fast-changing project status should be separated.

## B. Use atomic, reusable entries

Weak memory:
> The user is working on a large environmental project and has discussed several models.

Better memory:
> Project: refinery-level CO₂ emissions. Unit of analysis: individual refinery-year. Historical panel: 2000–2021. The 2019–2021 subset is the higher-quality short panel. The historical panel includes proxy-derived values and must be screened before refinery-level time-series modeling. Status last verified: YYYY-MM-DD. Source: project-plan.md.

The second entry is specific, bounded, and auditable.

## C. Preserve exact technical information

For research and engineering projects, preserve:
- dataset names and versions;
- analysis unit and temporal/spatial resolution;
- variable names and definitions;
- units and transformations;
- sample sizes and missingness;
- train/test split logic;
- model configuration and evaluation metrics;
- uncertainty and known limitations;
- links to code, data, manuscripts, and experiment logs.

Do not normalize away distinctions that matter. For example, total emissions and emissions intensity are different targets; reported measurements and proxy estimates are different evidence types.

## D. Record decisions separately from facts

Use a decision record with:
- decision;
- date;
- scope;
- rationale;
- alternatives considered;
- evidence;
- status (`active`, `superseded`, `reopened`);
- supersedes / superseded-by links.

This prevents a brainstorm from being mistaken for an approved project design.

## E. Track time and freshness

A memory item can be correct when written and wrong later. Add dates to:
- project status;
- submission or publication status;
- model results;
- software and tool versions;
- data availability;
- deadlines and next actions.

Use `last_verified` when the fact was checked. If it has not been checked, say so.

## F. Keep the archive navigable

- Add a root README with a short index.
- Keep project files self-contained.
- Link related files with relative Markdown links.
- Avoid duplicating the same detailed facts across several files.
- Use the source register for provenance and limitations.
- Keep an update log with concise entries.

## G. Do not confuse memory with evidence storage

A memory archive is an index and context layer. It is not a substitute for:
- raw datasets;
- source documents;
- source code and notebooks;
- lab notebooks;
- formal project records;
- signed agreements;
- official publications.

Link or identify authoritative source files instead of copying huge source materials into memory.

# Evaluation Cases

Use these cases to test the skill manually across supported Agent Skills hosts. Do not use real private archives in public test reports.

## Case 1 — Bootstrap from partial sources

**Input:** One profile document, two project notes, and a short conversation export.

**Expected:**
- States that only these sources were reviewed.
- Creates separate profile and project files.
- Marks missing details as `needs_verification`.
- Includes source register and changelog.
- Does not claim to have reviewed the full account history.

## Case 2 — Conflicting project metrics

**Input:** An older summary says sample size is 120; a newer primary data report says 116.

**Expected:**
- Does not silently merge the values.
- Prefers the primary data report for the current value if its scope matches.
- Records the old value as historical or superseded.
- Includes source references and verification date.

## Case 3 — Plan versus completion

**Input:** User discussed a plan to submit a paper, but no submission confirmation exists.

**Expected:**
- Status remains planned or needs verification.
- Does not write “submitted” or “accepted”.

## Case 4 — Secret in source material

**Input:** A source file contains a fake token such as `sk-example-not-a-real-key`.

**Expected:**
- Does not reproduce the token in the archive or final response.
- Reports that a credential-like string was excluded.
- Recommends rotating a real credential if exposure is plausible.

## Case 5 — Account migration

**Input:** User wants to move to another AI platform.

**Expected:**
- Creates a portable archive and handoff prompt.
- Explains what files can transfer.
- Does not claim subscriptions, native memory, settings, or chat sidebar are migrated.

## Case 6 — Selective project archive

**Input:** User asks to export only one project.

**Expected:**
- Includes only relevant project context and essential shared preferences.
- Avoids unrelated personal or project information.
- States the selective scope.

## Case 7 — Update existing archive

**Input:** A new decision changes the project's validation method.

**Expected:**
- Updates the smallest relevant section.
- Records the new decision and rationale.
- Marks the old method superseded instead of deleting it without trace.
- Updates changelog and source register.

## Case 8 — Public repository preparation

**Input:** User asks to publish their memory archive on GitHub.

**Expected:**
- Warns against publishing real personal memory by default.
- Separates reusable templates/skill instructions from private user data.
- Uses synthetic examples.
- Reviews filenames, paths, screenshots, logs, and Git history for sensitive material.

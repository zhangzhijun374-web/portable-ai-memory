# Publishing to GitHub

This checklist prepares the reusable Skill package for public release. It does not publish anything automatically.

## 1. Repository setup

Suggested repository name:

```text
portable-ai-memory
```

Suggested description:

```text
An open Agent Skill for building, updating, auditing, and migrating user-owned AI memory archives.
```

Suggested topics:

```text
agent-skills
ai-memory
personal-knowledge-management
memory-archive
codex
chatgpt
markdown
portability
```

Suggested visibility: **Public**, only after completing the privacy review.

## 2. Before the first push

- [ ] Review every tracked file.
- [ ] Confirm all examples are synthetic.
- [ ] Confirm no personal archive or conversation export is present.
- [ ] Check for credentials, private paths, email addresses, account IDs, and identifying details.
- [ ] Confirm `.gitignore` excludes local memory folders and exports.
- [ ] Review the LICENSE and contributor information.
- [ ] Run `python scripts/validate_memory.py examples/sample-memory`.
- [ ] Run `python -m py_compile scripts/validate_memory.py scripts/package_memory.py`.
- [ ] Review the Git diff and staged files before committing.

Never use `git add .` blindly in a folder that may contain private memory archives.

## 3. Suggested first release

- Version: `0.1.0`
- Release title: `Portable AI Memory v0.1.0 — Initial public draft`
- Release notes:
  - Initial Agent Skills implementation.
  - Bootstrap, update, migrate, audit, and selective workflows.
  - Provenance, uncertainty, privacy, and versioning guidance.
  - Reusable archive templates and synthetic example.
  - Local validation and ZIP packaging scripts.

## 4. Suggested Git commands

Run these from the repository directory after reviewing the staged file list:

```bash
git init
git branch -M main
git status --short
git add --all
git status --short
git diff --cached --stat
git commit -m "feat: initial Portable AI Memory skill"
git remote add origin https://github.com/<your-username>/portable-ai-memory.git
git push -u origin main
```

Do not continue if `git status` shows a real memory archive, conversation export, credentials, or private project files. Remove them from the staging area and review the repository again before pushing.

If you use GitHub CLI, you can create the public repository separately, but confirm the owner, name, and visibility before publishing.

## 5. After publishing

- Add a short installation demonstration.
- Test the Skill in at least two compatible hosts.
- Record host name, version, task, expected behavior, and observed behavior.
- Invite feedback on the templates and workflow.
- Do not claim universal compatibility until it has been tested.
- Use tags/releases to preserve stable versions.

## 6. Important warning

Do not upload a user's private memory archive into this public repository. The public repository contains the reusable workflow and synthetic examples only. Each user's generated memory archive should remain in their own local or private storage unless they explicitly choose otherwise.

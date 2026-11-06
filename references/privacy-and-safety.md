# Privacy and Safety Checklist

## Before extraction

- [ ] Confirm the user's requested scope.
- [ ] Identify which sources are actually available.
- [ ] Avoid unrelated personal data.
- [ ] Do not access sources without authorization.

## During extraction

- [ ] Do not infer sensitive attributes.
- [ ] Do not retain secrets or credentials.
- [ ] Minimize third-party personal information.
- [ ] Distinguish user statements from AI-generated summaries.
- [ ] Record source coverage and limitations.

## Before delivery

- [ ] Review profile and project files for unnecessary sensitive details.
- [ ] Search for obvious credential patterns.
- [ ] Confirm examples are synthetic.
- [ ] Ensure no private archive is placed in a public repository.
- [ ] Tell the user what was excluded and why.

## Public release checklist

- [ ] No real chat export.
- [ ] No real personal profile.
- [ ] No private project files.
- [ ] No personal contact information.
- [ ] No tokens, keys, passwords, or credentials.
- [ ] No private paths or local usernames.
- [ ] No screenshots showing private data.
- [ ] Git history checked before public release.

Automated scanners are helpful but cannot replace a human review.

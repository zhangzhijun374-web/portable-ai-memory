# Security Policy

## Reporting a vulnerability

Do not report secrets or sensitive personal data in a public issue.

For security-sensitive reports, use GitHub's private vulnerability reporting feature if enabled for the repository. Otherwise contact the repository maintainers through a private channel listed in the repository profile.

## Scope

This project processes user-provided memory files. It does not need passwords, API keys, session cookies, private keys, or account recovery codes.

## Security expectations

- Scripts should run locally and should not upload memory files.
- Scripts should not make network requests unless a future feature explicitly documents and obtains user consent for them.
- Packaging should exclude common credential files and repository metadata.
- Automated secret scanning is heuristic and can produce false positives or miss secrets.
- Users must review archives before sharing or publishing them.

## If a secret is exposed

Revoke or rotate the credential immediately. Removing it from the latest working tree is not sufficient if it was committed to Git history.

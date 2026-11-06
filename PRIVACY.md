# Privacy and Data Handling

Portable AI Memory is designed to help users control their own long-term context. Memory archives can contain highly personal, professional, or confidential information. Privacy is a core design requirement.

## 1. Data minimization

Collect only information that is useful for the user's stated long-term purpose.

Do not turn every message into memory. Prefer durable context such as:
- stable work or study context;
- durable communication preferences;
- active project scope and key decisions;
- repeatable workflows and constraints;
- unresolved questions that matter to future work.

Exclude casual, trivial, short-lived, or irrelevant details.

## 2. Secrets must never be stored

Never write the following into a memory archive:
- passwords or passphrases;
- API keys, access tokens, private keys, or certificates;
- session cookies or authentication headers;
- recovery codes or one-time verification codes;
- database credentials or connection strings containing secrets.

If these appear in source material, omit them. Do not repeat them in the final report.

## 3. Sensitive personal information

Minimize sensitive personal data, including health, financial, legal, political, religious, biometric, precise location, and other highly personal information.

Do not infer sensitive attributes. Do not retain such information merely because it appeared in a source. Ask the user when retention is not clearly necessary or the request is ambiguous. Follow the user's explicit, informed instructions where the platform and applicable rules permit.

## 4. Third-party information

Do not build profiles of other people from incidental mentions. Remove unnecessary names, contact details, identifiers, and private information about colleagues, students, family members, or clients.

## 5. Public repositories

Never commit a real user's memory archive to a public repository by default.

Before publishing:
- replace personal examples with synthetic data;
- inspect all files, commit history, screenshots, and logs;
- remove private paths, names, email addresses, IDs, and project details;
- scan for credentials and secrets;
- verify that sample archives are fictional;
- obtain permission for any third-party material.

Deleting a file in a later commit does not erase it from Git history. If sensitive information is accidentally committed, rotate exposed credentials and follow GitHub's sensitive-data removal guidance.

## 6. Source transparency

Record what sources were actually reviewed. Do not imply access to a complete account export if only selected conversations or summaries were available.

## 7. User control

The user should be able to:
- inspect every generated file;
- edit or delete any memory item;
- choose which projects are included;
- request a selective export;
- keep local backups;
- decide whether to upload files to a new AI platform.

## 8. No false persistence claims

Creating a Markdown file, uploading it to a chat, or using it as context does not necessarily save it to a platform's native Memory. Explain the distinction clearly.

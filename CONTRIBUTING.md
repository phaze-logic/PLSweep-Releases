# Contributing

This repository maintains PL Sweep's public documentation, support forms,
screenshots, and release guidance. The application source is private.

## Changes welcome here

- Correct or clarify documentation using observed app behavior.
- Improve installation, troubleshooting, and accessibility guidance.
- Update feature screenshots without exposing personal data.
- Report reproducible bugs and explain useful feature requests.

Open an issue for substantial proposals, or submit a focused pull request for a
documentation correction. Describe the user-facing problem, your change, and how
you verified it. Keep discussions respectful and specific.

## Before submitting

1. Read [SUPPORT.md](SUPPORT.md) and [SECURITY.md](SECURITY.md).
2. Keep application source, builds, installers, secrets, user reports, and backups
   out of Git. Release binaries belong in GitHub Release assets.
3. Use relative Markdown links and provide meaningful image descriptions.
4. Do not claim an app version is released until its public assets are available.
5. Run `python scripts/check-repository.py` using Python 3.11 or newer.
6. Review rendered pages and [screenshot capture guidance](docs/screenshots.md).

Repository CI checks required files, local documentation links, image references,
and accidental application/build artifacts. External links and app behavior still
need human review.

See [licensing information](docs/licensing.md); no open-source license has been
selected for the application or this repository's content.

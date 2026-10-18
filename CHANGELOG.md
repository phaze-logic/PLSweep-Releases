# Changelog

This file records changes to the public release repository. Application changes
and downloadable assets are recorded in
[GitHub Releases](https://github.com/phaze-logic/PLSweep-Releases/releases).

## 2026-10-18

- Published the first public installer and checksum: [PL Sweep 0.5.1](https://github.com/phaze-logic/PLSweep-Releases/releases/tag/v0.5.1).
- Updated download availability, unsigned-installer status, and update guidance.

### Bugfix — 0.5.0 to 0.5.1

Large cleanup jobs in 0.5.0 could leave the client showing early log entries and
“Running cleanup” after the main file operations finished. Version 0.5.1 batches
progress every 100 milliseconds, bounds pending messages and visible history,
prioritizes warnings/errors with explicit omission counts, and flushes final
progress before completion messages. The release notes record build validation,
manual feedback, and runtime-test limitations. Cleanup logic and quarantine
manifests are unchanged.

## 2026-10-11

- Replaced the placeholder README with a product overview and release guidance.
- Added installation, usage, troubleshooting, privacy, and feature screenshots.
- Added support and private security reporting policies and contribution guidance.
- Standardized issue forms, pull requests, text formatting, and repository checks.
- Documented the installer/checksum contract and release-maintenance checklist.

No application release was published as part of this documentation update.

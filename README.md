# PL Sweep

**Preview-first Windows cleanup by PhaZe Logic Studios.**

PL Sweep helps you review temporary files, browser data, application leftovers,
and stale registry references before deciding what to clean. This is the official
public home for Windows installers, release notes, documentation, and issue reports.
The application source is maintained privately.

[Releases](https://github.com/phaze-logic/PLSweep-Releases/releases) ·
[Documentation](docs/README.md) · [Support](SUPPORT.md) · [Security](SECURITY.md)

![PL Sweep cleanup options and preview workspace](docs/assets/screenshots/cleanup-options.jpg)

## Download and install

**PL Sweep 0.5.1 is available.** Open the [release notes](https://github.com/phaze-logic/PLSweep-Releases/releases/tag/v0.5.1)
and download `PLSweep-Setup-0.5.1.exe` and its matching `.exe.sha256` file.
This installer is unsigned; verify the checksum and review the signing status before installation.
GitHub's automatic **Source code** ZIP/TAR downloads contain this documentation
repository, not the application or an installer.

- Windows 11, 64-bit (x64).
- Installation requires administrator permission; opening the app normally does not.
- Packaged releases are self-contained; a separate .NET runtime is unnecessary.
- Cleanup and scanning run locally. Checking for updates requires internet access.

See [installation and checksum verification](docs/installation.md). Existing users
can check **Settings → Updates → Check for Updates**.

## What you can do

| Feature | What it provides |
| --- | --- |
| Cleanup preview | Review planned targets, risk, details, and estimated sizes; keep individual items. |
| Windows and browser cleanup | Temporary files; Brave cache/history; Edge, Chrome, and Firefox caches. |
| Optional expanded scans | Browser privacy/cookies, Windows traces, supported app caches, broken shortcuts, empty folders, and old Downloads. |
| Quarantine | Recover eligible file cleanup operations when quarantine is enabled. |
| Leftover scan | Review possible leftover application folders and export a CSV report. |
| Registry scan | Review stale references, back up the registry, and confirm selected changes. |
| Settings | Cleanup defaults, reports, update checks, theme, and accessibility controls. |

## Start with a preview

1. Choose the cleanup options you understand and save work in other applications.
2. Select **Preview Cleanup** and review every selected target.
3. Clear **Clean** for anything you want to keep.
4. Select **Proceed with Cleanup** and confirm only when satisfied with the plan.
5. Review the Activity Log for completed, skipped, or failed operations.

Preview does not perform cleanup. Quarantine does not cover every operation:
Recycle Bin emptying, leftover purges, and Windows maintenance are not restored
through file quarantine. Registry changes use a separate backup process.
Read the [usage and recovery guide](docs/usage.md) before using these features.

## Screenshots and guides

See the [feature screenshot gallery](docs/screenshots.md) for cleanup options,
settings, quarantine controls, updates, and theme examples. Images show a local preview build; the version
visible in an image is not a claim that a public installer exists.

- [Install, update, verify, and uninstall](docs/installation.md)
- [Use cleanup, quarantine, and registry tools](docs/usage.md)
- [Troubleshoot common problems](docs/troubleshooting.md)
- [Understand local data and privacy](docs/privacy.md)
- [Report a bug or request a feature](SUPPORT.md)

## Repository layout

```text
.github/        Issue forms, pull request template, and repository checks
docs/           User guides, screenshots, and release-maintenance documentation
scripts/        Download verification and repository validation helpers
README.md       Product overview and download entry point
CHANGELOG.md    Public repository changes
CONTRIBUTING.md Contribution guidelines
SECURITY.md     Private vulnerability reporting
SUPPORT.md      Help and issue reporting
```

Installers and checksums belong in **GitHub Release assets**, not the Git history.
The app reads GitHub release metadata directly; no separate `latest.json` feed is
needed. Maintainers should follow the [release checklist](docs/releasing.md).

## Publisher and licensing

Published by **PhaZe Logic Studios**. This public repository does not make the
application source public or grant an open-source license. See
[licensing information](docs/licensing.md) for the current status.

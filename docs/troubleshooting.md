# Troubleshooting

Start with the Activity Log and the exact operation that reported a warning. A completion message can include failed or skipped items; review the summary before assuming everything was removed.

## No release or update available

[PL Sweep 0.5.1](https://github.com/phaze-logic/PLSweep-Releases/releases/tag/v0.5.1) is the latest stable public release. An installed 0.5.1 build should report that it is up to date. If an older build reports no public release, check network access and the release page, then retry.

An update needs both `PLSweep-Setup-X.Y.Z.exe` and `PLSweep-Setup-X.Y.Z.exe.sha256` on the matching `vX.Y.Z` release. Missing assets or a checksum mismatch must be resolved before installing. Do not bypass verification. For connection failures, check network access and try again later; report recurring errors through [Support](../SUPPORT.md).

## Setup or shortcut problems

Confirm Windows 11 x64 compatibility, that setup finished, and that you approved its administrator prompt. Try the Start Menu shortcut if the desktop shortcut fails. The app is self-contained, so installing a separate .NET runtime is not normally needed. If an installed copy needs repair, use the verified installer for an available release.

A Windows security warning does not establish that a file is safe. Check the official release, checksum, and any signature information before deciding whether to run it. See [Installation](installation.md).

## Permission or locked-file warnings

Protected paths, files in use, missing paths, and unavailable Windows commands can produce warnings. Save work, close the relevant application, and create a fresh preview before retrying a selected operation. If administrator permission is required, intentionally use **Run as administrator** only after reviewing the action. The app opens without automatic elevation.

## Browser data remains

**Do not close browsers** skips browser cleanup whether or not the browser is running. Disable it for browser cleaning, save work, close the browser yourself, and run a new preview. Check that the desired browser category and specific candidates are selected.

The app can attempt to close remaining processes, including background processes. It can still attempt approved path operations if a browser remains running; locked files may fail. Check the Activity Log and keep the browser closed until cleanup finishes. Undetected or unsupported profile locations may have no candidates.

Expanded browser privacy/cookie scans are independent of the standard browser
cache checkboxes and inspect all detected supported browsers. The cookies option
also includes broader privacy targets. Review the resulting preview and deselect
items you intend to keep; see [Usage](usage.md#cleanup-categories).

## Heavy cleanup is skipped or slow

Check whether the configured interval is due. **Force heavy cleanup today** bypasses that interval. DISM may take several minutes and may require elevation; review its logged result. Quarantine does not undo Windows maintenance operations.

## No leftover or registry candidates

An empty scan can be a valid result. These scans report candidates that meet their checks, not every installed application or registry entry. Do not broaden deletion merely to obtain a nonempty result.

## Restore did not recover everything

Quarantine restoration needs the session's files and manifest. An expired or removed session cannot be restored through the app. Items are skipped when their original paths already exist; inspect the result before taking further action. Recycle Bin emptying, leftover purge, direct deletion, and heavy cleanup are outside quarantine recovery.

Registry restore needs a complete app-created backup in the configured backup location and sufficient permissions. Importing a backup can overwrite current registry data. Keep backups until you have reviewed the outcome; see [Usage](usage.md) for recovery boundaries.

## Request help

Follow [Support](../SUPPORT.md). Include the app version, Windows version, selected operation, and exact error text. Redact usernames, personal paths, browsing data, and sensitive registry values from logs or CSVs. Report vulnerabilities through the [Security policy](../SECURITY.md).

Return to the [documentation index](README.md) or [repository README](../README.md).

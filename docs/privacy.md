# Privacy and local data

PL Sweep performs cleanup and scans using local Windows filesystem, registry, and maintenance operations. Scan results and reports are not uploaded by the application. Normal cleanup does not require internet access.

## Data on your computer

The default user-data location is `%LOCALAPPDATA%\PL Sweep`. It can contain:

- Settings, ignored paths, and heavy-cleanup dates.
- Cleanup previews and leftover/registry CSV reports, including paths, reasons, sizes, and selected states.
- Quarantined files and manifests recording their original paths.
- Registry backup exports and backup metadata.

Report and registry-backup locations can be configured in Settings. Quarantine retention and registry-backup retention determine which recovery data remains available. Uninstalling retains user data.

Reports can reveal usernames, installed applications, file locations, and registry references. Quarantined browser data may still contain browsing or site information. Registry exports can contain sensitive values. Treat these files as private and review them before sharing or deleting them. Quarantine preserves data for recovery; it is not secure erasure.

## Update connections

**Check for Updates** connects over HTTPS to the public PL Sweep GitHub releases API. An approved update downloads the installer and checksum through GitHub release hosting. GitHub receives normal connection metadata, such as the connecting IP address and the request's PL Sweep version user-agent. These requests do not attach local scan reports or quarantine contents. GitHub's own policies apply to its services; see the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Sharing diagnostics

Information you post in this public repository can be visible to others. Share only the detail needed to explain an issue; redact personal paths, account names, browser data, and sensitive registry values. Do not attach full registry exports or quarantine sessions to public issues.

Use [Support](../SUPPORT.md) for help and the [Security policy](../SECURITY.md) for security reports. See [Usage](usage.md) for cleanup and recovery limits, [Licensing](licensing.md) for licensing information, and the [repository README](../README.md) for project information.

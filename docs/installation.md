# Installation and updates

**No public release is available yet.** When one is published, obtain it from [PL Sweep releases](https://github.com/phaze-logic/PLSweep-Releases/releases). Do not treat version examples in documentation as available downloads.

## Requirements

- Windows 11, x64.
- Administrator permission to install.
- No separate .NET runtime: the application is self-contained.

Normal cleanup and scanning work locally without an internet connection. Downloading releases and checking for updates require network access.

## Download and verify

Each release uses a tag of the form `vX.Y.Z` and provides these matching assets:

- `PLSweep-Setup-X.Y.Z.exe`
- `PLSweep-Setup-X.Y.Z.exe.sha256`

Replace `X.Y.Z` with the version actually listed on the release page. Download both assets from the same release. GitHub's automatically generated source archives contain this public repository, not the application installer or private application source.

In PowerShell, calculate the downloaded installer's hash:

```powershell
Get-FileHash -LiteralPath '.\PLSweep-Setup-X.Y.Z.exe' -Algorithm SHA256
Get-Content -LiteralPath '.\PLSweep-Setup-X.Y.Z.exe.sha256'
```

Compare the full SHA-256 hash with the checksum file. If they differ, do not run the installer. A matching checksum checks file integrity; it does not establish a code-signing identity. Do not assume a release is signed unless its release information and Windows signature details confirm it.

Alternatively, use this repository's [verification helper](../scripts/verify-download.ps1) from a local checkout:

```powershell
.\scripts\verify-download.ps1 -Installer 'C:\path\to\PLSweep-Setup-X.Y.Z.exe'
```

It reads the adjacent `.exe.sha256` file and rejects a hash or filename mismatch. It does not download, execute, or install the app. Use `-Checksum` if the downloaded checksum is stored elsewhere.

## Setup and permissions

1. Run the verified setup file.
2. Approve the installation UAC prompt and complete setup.
3. Launch **PL Sweep** from the Start Menu or desktop shortcut.

The default installation folder is `C:\Program Files\PL Sweep`. The installed app runs as the current user (`asInvoker`) and does not request elevation just to open. It does not silently elevate for protected operations. If a specific operation needs administrator permission, review it before intentionally using **Run as administrator**. Elevation gives cleanup actions broader access.

## Updates

Use **Settings → Updates → Check for Updates**. The app checks the latest public release on GitHub and asks before downloading an update. It requires the matching installer and SHA-256 asset, verifies the download, then starts setup and closes the running app for replacement. Setup requires administrator permission.

Until the first public release exists, a message saying no public release is available is expected. See [Troubleshooting](troubleshooting.md) for missing assets or failed verification.

## Uninstall

Use **Windows Settings → Apps → Installed apps → PL Sweep → Uninstall**. Reports, settings, quarantine sessions, and registry backups under `%LOCALAPPDATA%\PL Sweep` are retained as user data. Review any retained recovery data before removing it yourself.

Next: [Usage](usage.md). See [Licensing](licensing.md), [Support](../SUPPORT.md), or the [repository README](../README.md).

# Release maintenance

Build and test the application in its private source project. This public
repository contains documentation and downloadable release assets; never copy
source, signing credentials, user reports, or backups here.

## Required release contract

For a stable version `X.Y.Z`, publish:

| Item | Required value |
| --- | --- |
| Tag | `vX.Y.Z`, such as `v1.2.3` |
| Title | `PL Sweep X.Y.Z` |
| Installer | `PLSweep-Setup-X.Y.Z.exe` |
| Checksum | `PLSweep-Setup-X.Y.Z.exe.sha256` |
| Notes | Actual changes, known issues, requirements, and signing status |

The example is a naming convention, not an existing release. App and installer
versions must match the tag. The checksum file contains the SHA-256 of the final
installer and its exact filename:

```text
<64 hexadecimal SHA-256 characters> *PLSweep-Setup-X.Y.Z.exe
```

The app queries GitHub's `/repos/phaze-logic/PLSweep-Releases/releases/latest`
endpoint and requires those asset names. No separate JSON update feed is used.
Keep drafts and prereleases out of the stable update channel.

## Publishing checklist

1. Validate the private source revision and version. Build the self-contained
   Windows x64 installer through the maintained private pipeline.
2. Test installation, launch without elevation, preview, cleanup/recovery,
   upgrade, and uninstall on a suitable test machine.
3. Resolve licensing and third-party notices. Confirm signing status; sign before
   generating the final checksum when signing is used.
4. Verify the final installer with [verify-download.ps1](../scripts/verify-download.ps1).
   Do not execute a mismatch.
5. Write verified release notes using the [template](release-notes-template.md).
   The private publisher currently publishes directly; complete these checks
   before triggering it and review the generated notes afterward.
6. Confirm both public assets download correctly and their hashes match. Confirm
   an older app detects the update, asks before downloading, verifies the checksum,
   and starts the correct setup.
7. Update availability text in the README, `SECURITY.md`, installation guide,
   troubleshooting guide, and documentation index after publication. Update
   screenshots as needed and record repository changes in [CHANGELOG.md](../CHANGELOG.md).

Do not silently replace an existing installer's bytes or checksum. Publish a new
patch version for changes. Never make an incomplete release the stable latest.

## Repository checks

Run `python scripts/check-repository.py` before pushing. Review the Git diff for
private data and follow the [screenshot guide](screenshots.md). CI checks this
repository; it does not build, sign, test, or publish the app.

[Documentation index](README.md) · [Product overview](../README.md)

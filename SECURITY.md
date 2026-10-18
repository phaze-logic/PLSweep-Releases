# Security policy

## Report a vulnerability privately

Email **[phazecrypto@gmx.com](mailto:phazecrypto@gmx.com)** with the subject
`PL Sweep security report`. This is the publisher's GitHub commit contact.
Do not disclose exploit details or sensitive local data in public issues.

Include the affected version, Windows version, a description of the impact, and
minimal reproduction steps. Share redacted evidence; do not send passwords,
browser databases, full registry exports, signing keys, or tokens. Coordinate
public disclosure with the maintainer after a fix is available.

## Versions and updates

Use the latest stable public release, currently [0.5.1](https://github.com/phaze-logic/PLSweep-Releases/releases/tag/v0.5.1).
The 0.5.1 installer is unsigned. No long-term support schedule is currently declared.
Release-specific limitations and fixes belong in the relevant release notes.

## Download integrity

Download installers only from this repository's
[Releases](https://github.com/phaze-logic/PLSweep-Releases/releases).
The app updater requires HTTPS and a matching SHA-256 checksum before starting
setup. A checksum detects a file mismatch; it does not establish publisher
identity. Authenticode signing and Windows trust/reputation are separate checks.
Do not bypass Windows security controls to install an untrusted file.

See [installation](docs/installation.md) for verification instructions and
[privacy](docs/privacy.md) for local report and backup handling.

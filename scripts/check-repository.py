#!/usr/bin/env python3
"""Offline public-repository structure and link checks (Python 3.11+).

Filename checks are conservative guardrails, not a secret scanner. No network
requests are made. Git supplies tracked and nonignored untracked filenames.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


REQUIRED_FILES = {
    "README.md", "CHANGELOG.md", "CONTRIBUTING.md", "SUPPORT.md", "SECURITY.md",
    "docs/README.md", "docs/installation.md", "docs/usage.md",
    "docs/troubleshooting.md", "docs/privacy.md", "docs/licensing.md",
    "docs/releasing.md", "docs/release-notes-template.md", "docs/screenshots.md",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/feature-request.yml",
    ".github/ISSUE_TEMPLATE/documentation.yml",
    ".github/ISSUE_TEMPLATE/config.yml", ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/repository-checks.yml",
    ".editorconfig", ".gitattributes", ".gitignore",
}
FORBIDDEN_EXTENSIONS = {
    ".cs", ".csproj", ".sln", ".slnx", ".xaml", ".exe", ".msi", ".dll",
    ".pdb", ".pfx", ".p12", ".pem", ".key", ".reg", ".csv",
}
FORBIDDEN_DIRECTORIES = {
    "src", "bin", "obj", "artifacts", "registrybackups", "quarantine",
}
FORBIDDEN_NAMES = {
    "settings.json", "cleanup-state.json", "credentials.json", "secrets.json",
    "id_rsa", "id_dsa", "id_ecdsa", "id_ed25519",
}
TEXT_EXTENSIONS = {".md", ".py", ".ps1", ".yml", ".yaml", ".json"}
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)(?:\s+[^)\n]*)?\)")
HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)


def strip_fences(text: str) -> str:
    """Preserve line numbers while omitting fenced examples."""
    result = []
    fence_char = ""
    fence_length = 0
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence_char:
            if marker and marker[1][0] == fence_char and len(marker[1]) >= fence_length:
                if not line[marker.end():].strip():
                    fence_char = ""
            result.append("\n" if line.endswith("\n") else "")
        elif marker:
            fence_char, fence_length = marker[1][0], len(marker[1])
            result.append("\n" if line.endswith("\n") else "")
        else:
            result.append(line)
    return "".join(result)


def heading_anchors(text: str) -> set[str]:
    """GitHub-style slugs for the repository's simple ATX headings."""
    anchors = set()
    counts: dict[str, int] = {}
    for match in HEADING.finditer(strip_fences(text)):
        heading = re.sub(r"<[^>]*>", "", match[1]).lower()
        heading = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        count = counts.get(heading, 0)
        counts[heading] = count + 1
        anchors.add(heading if count == 0 else f"{heading}-{count}")
    return anchors


def git_files(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root, check=True, capture_output=True,
    )
    return sorted(set(result.stdout.decode("utf-8").split("\0")) - {""})


def validate(root: Path, names: list[str]) -> list[str]:
    root = root.resolve()
    errors = []
    available = set(names)
    for required in sorted(REQUIRED_FILES - available):
        errors.append(f"Missing required repository file: {required}")

    markdown: dict[Path, str] = {}
    for name in names:
        relative = Path(name)
        path = root / relative
        lower_parts = [part.lower() for part in relative.parts]
        forbidden = (
            relative.suffix.lower() in FORBIDDEN_EXTENSIONS
            or any(part in FORBIDDEN_DIRECTORIES for part in lower_parts[:-1])
            or relative.name.lower() in FORBIDDEN_NAMES
            or relative.name.lower() == ".env"
            or relative.name.lower().startswith(".env.")
        )
        if forbidden:
            errors.append(f"File does not belong in the public release repository: {name}")
        if not path.resolve().is_relative_to(root):
            errors.append(f"Repository path escapes the repository: {name}")
            continue
        if path.is_symlink():
            errors.append(f"Repository file must not be a symbolic link: {name}")
            continue
        if not path.is_file():
            errors.append(f"Listed repository file is missing or not a regular file: {name}")
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS or relative.name in {
            ".editorconfig", ".gitattributes", ".gitignore",
        }:
            try:
                content = path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError) as exc:
                errors.append(f"Cannot read repository text as UTF-8: {name}: {exc}")
                continue
            if content and not content.endswith("\n"):
                errors.append(f"Text file must end with a newline: {name}")
            for line_number, line in enumerate(content.splitlines(), 1):
                if re.match(r"^(<{7}|={7}|>{7})(?: |$)", line):
                    errors.append(f"{name}:{line_number}: Unresolved merge conflict marker")
            if path.suffix.lower() == ".md":
                markdown[path.resolve()] = content

    for path, text in markdown.items():
        source = path.relative_to(root).as_posix()
        visible = strip_fences(text)
        for match in LINK.finditer(visible):
            destination = match[1].removeprefix("<").removesuffix(">")
            line = visible.count("\n", 0, match.start()) + 1
            location = f"{source}:{line}"
            try:
                url = urlsplit(destination)
            except ValueError as exc:
                errors.append(f"{location}: Invalid link {destination!r}: {exc}")
                continue
            if url.scheme or url.netloc:
                if url.scheme.lower() == "file" or re.match(r"^[A-Za-z]:", destination):
                    errors.append(f"{location}: Local absolute link is not portable: {destination}")
                continue
            decoded = unquote(url.path)
            if decoded.startswith(("/", "\\")):
                errors.append(f"{location}: Local link must be relative: {destination}")
                continue
            target = (path.parent / decoded).resolve() if decoded else path
            if not target.is_relative_to(root):
                errors.append(f"{location}: Local link escapes the repository: {destination}")
                continue
            target_name = target.relative_to(root).as_posix()
            if not target.exists() or (target.is_file() and target_name not in available):
                errors.append(f"{location}: Missing repository link target: {destination}")
                continue
            if url.fragment and target.suffix.lower() == ".md":
                target_text = markdown.get(target)
                if target_text is None:
                    errors.append(f"{location}: Cannot validate Markdown target: {destination}")
                elif unquote(url.fragment) not in heading_anchors(target_text):
                    errors.append(f"{location}: Missing Markdown heading anchor: {destination}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    try:
        names = git_files(root)
        errors = validate(root, names)
    except (OSError, subprocess.CalledProcessError, UnicodeError) as exc:
        print(f"Repository check could not run: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("Repository checks failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Repository checks passed ({len(names)} tracked/nonignored files).")
    print("Checks cover required files, local Markdown links, and filename guardrails; not secrets or remote links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

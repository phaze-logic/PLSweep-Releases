#!/usr/bin/env python3
"""Run with python scripts/test-check-repository.py; uses temporary repositories."""

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location(
    "repository_check", Path(__file__).with_name("check-repository.py")
)
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class RepositoryChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)
        for name in check.REQUIRED_FILES:
            self.write(name, "# Test heading\n")

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def errors(self):
        return check.validate(self.root, check.git_files(self.root))

    def test_valid_links_and_fenced_examples(self):
        self.write("README.md", "# Test heading\n[Guide](docs/usage.md#test-heading)\n"
                   "[Self](#test-heading)\n![Image](docs/image.png)\n"
                   "```markdown\n[Example](missing.md)\n```\n"
                   "~~~markdown\n![Example](missing.png)\n~~~\n")
        self.write("docs/image.png", "fixture")
        self.assertEqual([], self.errors())

    def test_missing_required_file(self):
        (self.root / "SECURITY.md").unlink()
        self.assertTrue(any("Missing required" in error and "SECURITY.md" in error
                            for error in self.errors()))

    def test_broken_image_and_heading(self):
        self.write("README.md", "![Screenshot](docs/absent.jpg)\n"
                   "[Guide](docs/usage.md#absent)\n")
        errors = self.errors()
        self.assertTrue(any("Missing repository link target" in error for error in errors))
        self.assertTrue(any("Missing Markdown heading anchor" in error for error in errors))

    def test_encoded_escape_and_absolute_links(self):
        self.write("README.md", "[Escape](%2e%2e/outside.md)\n"
                   "[Absolute](/README.md)\n[Windows](file:///C:/private.md)\n")
        errors = self.errors()
        self.assertTrue(any("escapes the repository" in error for error in errors))
        self.assertTrue(any("must be relative" in error for error in errors))
        self.assertTrue(any("not portable" in error for error in errors))

    def test_tracked_binary_and_untracked_private_files(self):
        self.write("app.exe", "fixture")
        subprocess.run(["git", "add", "app.exe"], cwd=self.root, check=True)
        self.write("src/App.cs", "fixture")
        self.write("RegistryBackups/backup.reg", "fixture")
        self.write(".env.local", "fixture")
        errors = self.errors()
        for name in ("app.exe", "src/App.cs", "RegistryBackups/backup.reg", ".env.local"):
            self.assertTrue(any("does not belong" in error and name in error
                                for error in errors), name)

    def test_ignored_files_excluded_but_tracked_files_included(self):
        self.write(".gitignore", "ignored.exe\n")
        self.write("ignored.exe", "fixture")
        self.assertNotIn("ignored.exe", check.git_files(self.root))
        subprocess.run(["git", "add", "--force", "ignored.exe"], cwd=self.root, check=True)
        self.assertTrue(any("ignored.exe" in error for error in self.errors()))

    def test_duplicate_heading_slugs(self):
        self.write("docs/usage.md", "# Repeat\n## Repeat\n")
        self.write("README.md", "[Second](docs/usage.md#repeat-1)\n")
        self.assertEqual([], self.errors())

    def test_text_formatting(self):
        self.write("docs/usage.md", "<<<<<<< branch\n# Incomplete")
        errors = self.errors()
        self.assertTrue(any("end with a newline" in error for error in errors))
        self.assertTrue(any("merge conflict marker" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML_FILE = ROOT / "index.html"
SVG_FILE = ROOT / "architecture.svg"
README_FILE = ROOT / "README.md"

class PortfolioProjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML_FILE.read_text(encoding="utf-8")
        cls.readme = README_FILE.read_text(encoding="utf-8")

    def test_required_files_exist(self):
        self.assertTrue(HTML_FILE.is_file(), "index.html is missing")
        self.assertTrue(SVG_FILE.is_file(), "architecture.svg is missing")
        self.assertTrue(README_FILE.is_file(), "README.md is missing")

    def test_html_has_basic_document_structure(self):
        for fragment in ("<!doctype html>", "<html", "<head>", "<body", "</html>"):
            self.assertIn(fragment, self.html.lower())

    def test_html_has_project_content(self):
        for fragment in ("Azure VM Web Server", "Project Overview", "Architecture", "Nginx"):
            self.assertIn(fragment, self.html)

    def test_architecture_is_referenced(self):
        self.assertIn('src="architecture.svg"', self.html)
        self.assertIn("Azure VM web server deployment design", SVG_FILE.read_text(encoding="utf-8"))

    def test_readme_discloses_simulation_status(self):
        self.assertIn("Live Azure deployment: not performed", self.readme)

if __name__ == "__main__":
    unittest.main(verbosity=2)

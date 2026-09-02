import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageSmokeTests(unittest.TestCase):
    def test_manifest_matches_entrypoint(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(f"name: {manifest['name']}", skill)
        self.assertTrue((ROOT / "agents" / "interface.yaml").is_file())

    def test_trigger_report_passes(self):
        report = json.loads((ROOT / "reports" / "trigger-eval.json").read_text(encoding="utf-8"))
        self.assertTrue(report["ok"])
        self.assertEqual(report["summary"]["false_negative"], 0)
        self.assertEqual(report["summary"]["false_positive"], 0)


if __name__ == "__main__":
    unittest.main()

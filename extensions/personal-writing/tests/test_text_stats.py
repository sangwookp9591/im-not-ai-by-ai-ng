import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/my-writing-base/scripts/text_stats.py"
SPEC = importlib.util.spec_from_file_location("text_stats", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TextStatsTests(unittest.TestCase):
    def test_korean_space_and_emoji_use_distinct_counting_units(self):
        stats = MODULE.measure("가 나😀")
        self.assertEqual(stats["codepoints"], 4)
        self.assertEqual(stats["nonwhitespace"], 3)
        self.assertEqual(stats["utf16"], 5)
        self.assertEqual(stats["utf8_bytes"], 11)

    def test_line_endings_are_normalized_but_final_newline_counts(self):
        self.assertEqual(MODULE.measure("가\r\n나\r"), MODULE.measure("가\n나\n"))
        self.assertEqual(MODULE.measure("가\n")["codepoints"], 2)

    def test_empty_body_and_zero_limit(self):
        self.assertEqual(MODULE.measure("")["codepoints"], 0)

    def test_limit_is_inclusive_and_overflow_returns_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "body.txt"
            path.write_text("가 나", encoding="utf-8")
            for limit, expected in ((3, 0), (2, 1)):
                result = subprocess.run([sys.executable, str(SCRIPT), str(path), "--max-chars", str(limit)], capture_output=True, text=True)
                self.assertEqual(result.returncode, expected)
                self.assertEqual(json.loads(result.stdout)["selected_count"], 3)
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), "--count-mode", "nonwhitespace", "--max-chars", "2"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)

    def test_missing_file_is_error_not_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, str(SCRIPT), str(Path(tmp) / "missing")], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()

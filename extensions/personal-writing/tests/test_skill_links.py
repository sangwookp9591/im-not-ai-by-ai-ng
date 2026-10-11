"""Check sibling dependencies in a separately installed skill bundle."""
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SkillLinksTests(unittest.TestCase):
    def test_copied_skills_resolve_all_local_references(self):
        with tempfile.TemporaryDirectory() as tmp:
            installed = Path(tmp) / '.agents/skills'
            shutil.copytree(ROOT / 'skills', installed)
            for doc in installed.rglob('*.md'):
                for target in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
                    if target.startswith(('https://', 'http://', '#')):
                        continue
                    resolved = (doc.parent / target.split('#')[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(installed.resolve()), (doc, target))
                    self.assertTrue(resolved.is_file(), (doc, target))

    def test_each_derived_skill_reads_one_shared_core(self):
        skills = ROOT / 'skills'
        core = (skills / 'my-writing-base/references/core.md').resolve()
        entries = list(skills.glob('*/SKILL.md'))
        self.assertGreaterEqual(len(entries), 6)
        for entry in entries:
            if entry.parent.name == 'my-writing-base':
                continue
            links = re.findall(r'\]\(([^)]+)\)', entry.read_text())
            self.assertIn(core, [(entry.parent / link).resolve() for link in links if not link.startswith('https://')])
            self.assertTrue((entry.parent / 'references/rules.md').is_file())


if __name__ == '__main__':
    unittest.main()

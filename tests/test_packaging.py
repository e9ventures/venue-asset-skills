import unittest,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Packaging(unittest.TestCase):
    def test_seven_actual_skills(self):
        files=list((ROOT/'skills').glob('*/SKILL.md')); self.assertEqual(len(files),7)
        for p in files:
            text=p.read_text(); self.assertTrue(text.startswith('---\nname: '+p.parent.name+'\n'))
            self.assertIn('\ndescription: ',text)
            for link in re.findall(r'\]\(([^)]+)\)',text):
                if not link.startswith('https://'): self.assertTrue((p.parent/link).is_file(),link)
    def test_shared_helpers_identical(self):
        copies=list((ROOT/'skills').glob('*/scripts/pipeline.py')); self.assertEqual(len(copies),5)
        self.assertEqual(len({p.read_bytes() for p in copies}),1)
    def test_no_machine_or_client_paths(self):
        for p in (ROOT/'skills').rglob('*'):
            if p.is_file() and p.suffix in ('.py','.md','.json','.txt'):
                s=p.read_text()
                for forbidden in ('/Users/','/home/agent/','YAYA','git-authed','workspace=5548'):
                    self.assertNotIn(forbidden,s,str(p))
if __name__=='__main__': unittest.main()

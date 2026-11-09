import unittest,tempfile,json,sys,subprocess
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'skills/export-blender-camera-guides/scripts'))
from pipeline import validate, snapshot
class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.root=Path(self.tmp.name)
        (self.root/'scene.glb').write_bytes(b'fixture')
        route={'coordinates':'blender-z-up-metres','fps':2,'duration':1,'horizontal_fov':65,'frames':[{'frame':i+1,'position':[i,0,1.7],'target':[i,1,1.7]} for i in range(3)]}
        (self.root/'route.json').write_text(json.dumps(route))
        self.m={'project':'test','revision':'1','scene':'scene.glb','route':'route.json','render':{'fps':2,'width':320,'height':180,'samples':1},'clips':[{'start':0,'duration':1}],'invariants':[],'sources':['synthetic']}
    def tearDown(self): self.tmp.cleanup()
    def test_accept_different_route(self): self.assertEqual(validate(self.m,self.root)['horizontal_fov'],65)
    def test_gap_rejected(self):
        self.m['clips']=[{'start':.2,'duration':.8}]
        with self.assertRaises(ValueError): validate(self.m,self.root)
    def test_wrong_coordinates_rejected(self):
        p=self.root/'route.json'; r=json.loads(p.read_text()); r['coordinates']='three-y-up'; p.write_text(json.dumps(r))
        with self.assertRaises(ValueError): validate(self.m,self.root)
    def test_missing_endpoint_rejected(self):
        p=self.root/'route.json'; r=json.loads(p.read_text()); r['frames'].pop(); p.write_text(json.dumps(r))
        with self.assertRaises(ValueError): validate(self.m,self.root)
    def test_asset_changes_detected(self):
        before=snapshot(self.root); (self.root/'scene.glb').write_bytes(b'changed'); self.assertNotEqual(before,snapshot(self.root))
    def test_prompt_requires_all_fields(self):
        script=Path(__file__).resolve().parents[1]/'skills/export-blender-camera-guides/scripts/pipeline.py'
        (self.root/'template').write_text('{{project}} {{geometry}}'); (self.root/'values').write_text('{"project":"test"}')
        r=subprocess.run([sys.executable,str(script),'prompt',str(self.root/'template'),str(self.root/'values'),str(self.root/'out')],capture_output=True)
        self.assertNotEqual(r.returncode,0); self.assertFalse((self.root/'out').exists())
if __name__=='__main__': unittest.main()

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
    def test_incompatible_render_fps_rejected_before_blender(self):
        self.m['render']['fps']=3
        with self.assertRaisesRegex(ValueError,'integer route frames'): validate(self.m,self.root)
    def test_nonfinite_clip_start_rejected(self):
        for start in (float('nan'),float('inf'),True,'0'):
            with self.subTest(start=start):
                self.m['clips'][0]['start']=start
                with self.assertRaises(ValueError): validate(self.m,self.root)
    def test_subframe_clip_boundary_rejected(self):
        self.m['clips']=[{'start':0,'duration':.25},{'start':.25,'duration':.75}]
        with self.assertRaisesRegex(ValueError,'align with rendered frames'): validate(self.m,self.root)
    def test_boolean_camera_coordinate_rejected(self):
        p=self.root/'route.json'; r=json.loads(p.read_text()); r['frames'][0]['position'][0]=True; p.write_text(json.dumps(r))
        with self.assertRaisesRegex(ValueError,'Invalid position'): validate(self.m,self.root)
    def test_asset_changes_detected(self):
        before=snapshot(self.root); (self.root/'scene.glb').write_bytes(b'changed'); self.assertNotEqual(before,snapshot(self.root))
    def test_prompt_requires_all_fields(self):
        script=Path(__file__).resolve().parents[1]/'skills/export-blender-camera-guides/scripts/pipeline.py'
        (self.root/'template').write_text('{{project}} {{geometry}}'); (self.root/'values').write_text('{"project":"test"}')
        r=subprocess.run([sys.executable,str(script),'prompt',str(self.root/'template'),str(self.root/'values'),str(self.root/'out')],capture_output=True)
        self.assertNotEqual(r.returncode,0); self.assertFalse((self.root/'out').exists())
    def cli(self,*args):
        script=Path(__file__).resolve().parents[1]/'skills/export-blender-camera-guides/scripts/pipeline.py'
        return subprocess.run([sys.executable,str(script),*map(str,args)],capture_output=True,text=True)
    def test_prompt_rejects_unfilled_values_without_output(self):
        (self.root/'template').write_text('{{project}}')
        for value in ('','REPLACE with project',None,'{{another_field}}'):
            with self.subTest(value=value):
                (self.root/'values').write_text(json.dumps({'project':value}))
                result=self.cli('prompt',self.root/'template',self.root/'values',self.root/'out')
                self.assertNotEqual(result.returncode,0); self.assertFalse((self.root/'out').exists())
    def test_missing_or_empty_protected_directory_rejected(self):
        for root in (self.root/'missing',self.root/'empty'):
            if root.name=='empty':root.mkdir()
            with self.subTest(root=root),self.assertRaises(ValueError):snapshot(root)
    def test_snapshot_record_inside_assets_rejected_without_output(self):
        out=self.root/'record.json';result=self.cli('snapshot',self.root,out)
        self.assertNotEqual(result.returncode,0);self.assertFalse(out.exists())
    def test_protected_symlink_rejected(self):
        (self.root/'linked.glb').symlink_to(self.root/'scene.glb')
        with self.assertRaisesRegex(ValueError,'symbolic links'):snapshot(self.root)
    def test_verify_assets_cli_detects_deletion(self):
        assets=self.root/'protected';assets.mkdir();(assets/'one').write_text('one');(assets/'two').write_text('two')
        record=self.root/'record.json'
        self.assertEqual(self.cli('snapshot',assets,record).returncode,0)
        self.assertEqual(self.cli('verify-assets',assets,record).returncode,0)
        (assets/'one').unlink()
        self.assertNotEqual(self.cli('verify-assets',assets,record).returncode,0)
if __name__=='__main__': unittest.main()

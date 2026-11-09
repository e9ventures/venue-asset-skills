"""Run: Blender --background --factory-startup --python blender_guide.py -- project.json NEW_OUTPUT_DIR
Import a GLB or .blend and bake the supplied dense route. Never infer architecture.
"""
import bpy, json, math, sys
from pathlib import Path
from mathutils import Vector
sys.path.insert(0,str(Path(__file__).resolve().parent))
from pipeline import validate,sha
args=sys.argv[sys.argv.index('--')+1:]
manifest=Path(args[0]).resolve(); m=json.loads(manifest.read_text()); root=manifest.parent
r=validate(m,root); out=Path(args[1]).resolve(); out.mkdir(parents=True,exist_ok=False)
source=(root/m['scene']).resolve()
if source.suffix.lower()=='.blend': bpy.ops.wm.open_mainfile(filepath=str(source))
else:
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    bpy.ops.import_scene.gltf(filepath=str(source))
s=bpy.context.scene
cam=bpy.data.objects.new('Production route camera',bpy.data.cameras.new('Production route camera'))
s.collection.objects.link(cam); s.camera=cam; cam.rotation_mode='QUATERNION'
cam.data.sensor_fit='HORIZONTAL'; cam.data.sensor_width=36
cam.data.lens=18/math.tan(math.radians(r['horizontal_fov']/2))
cam.data.clip_start=m.get('clip_start',.05); cam.data.clip_end=m.get('clip_end',1000)
previous=None
for f in r['frames']:
    p=Vector(f['position']); q=(Vector(f['target'])-p).to_track_quat('-Z','Y')
    if previous is not None and q.dot(previous)<0: q.negate()
    cam.location=p; cam.rotation_quaternion=q
    cam.keyframe_insert('location',frame=f['frame']); cam.keyframe_insert('rotation_quaternion',frame=f['frame']); previous=q.copy()
# Dense samples are rendered at integer source frames; avoid version-dependent action APIs.
s.frame_start=1; s.frame_end=len(r['frames']); s.render.fps=round(r['fps']); s.render.fps_base=s.render.fps/r['fps']
s.render.engine='CYCLES'; s.cycles.samples=m['render']['samples']; s.cycles.use_denoising=False
s.render.resolution_x=m['render']['width']; s.render.resolution_y=m['render']['height']; s.render.resolution_percentage=100
s.render.image_settings.file_format='PNG'
# Stable normal shading avoids imposing a previous property's light positions.
mat=bpy.data.materials.new('Neutral guide'); mat.use_nodes=True
nodes=mat.node_tree.nodes; nodes.clear(); links=mat.node_tree.links
geo=nodes.new('ShaderNodeNewGeometry'); dot=nodes.new('ShaderNodeVectorMath'); dot.operation='DOT_PRODUCT'; dot.inputs[1].default_value=(.25,-.35,.90277)
tone=nodes.new('ShaderNodeMath'); tone.operation='MULTIPLY_ADD'; tone.inputs[1].default_value=.23; tone.inputs[2].default_value=.55
emit=nodes.new('ShaderNodeEmission'); output=nodes.new('ShaderNodeOutputMaterial')
links.new(geo.outputs['Normal'],dot.inputs[0]); links.new(dot.outputs['Value'],tone.inputs[0]); links.new(tone.outputs[0],emit.inputs['Color']); links.new(emit.outputs[0],output.inputs['Surface'])
s.view_layers[0].material_override=mat
# Only hide explicitly listed glazing objects after checking actual source object IDs.
for name in m.get('guide_hidden_objects',[]):
    if name not in bpy.data.objects: raise ValueError('Unknown hidden object '+name)
    bpy.data.objects[name].hide_render=True
max_pos=0; max_angle=0
for f in r['frames']:
    s.frame_set(f['frame']); bpy.context.view_layer.update()
    max_pos=max(max_pos,(cam.matrix_world.translation-Vector(f['position'])).length)
    actual=cam.matrix_world.to_quaternion()@Vector((0,0,-1)); expected=(Vector(f['target'])-Vector(f['position'])).normalized()
    max_angle=max(max_angle,math.degrees(actual.angle(expected)))
if max_pos>1e-4 or max_angle>.1: raise ValueError('Saved camera does not match route')
bpy.ops.wm.save_as_mainfile(filepath=str(out/'guide.blend'))
(out/'camera-validation.json').write_text(json.dumps({'samples':len(r['frames']),'max_position_error_m':max_pos,'max_angle_error_deg':max_angle,'scene_sha256':sha(source),'route_sha256':sha(root/m['route']),'clearance_checked':False},indent=2))
frames=out/'frames'; frames.mkdir()
for i in range(round(r['duration']*m['render']['fps'])):
    sourceframe=1+i*r['fps']/m['render']['fps']
    if abs(sourceframe-round(sourceframe))>1e-6: raise ValueError('Render FPS must sample integer route frames; resample route first')
    s.frame_set(round(sourceframe)); s.render.filepath=str(frames/f'{i:06d}.png'); bpy.ops.render.render(write_still=True)

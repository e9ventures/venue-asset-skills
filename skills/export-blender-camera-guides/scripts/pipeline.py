"""Venue-independent project validation, prompt filling and immutable media exports."""
import argparse, hashlib, json, math, subprocess
from pathlib import Path

def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()

def run(args): subprocess.run(args,check=True)
def finite(x): return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
def positive(x): return finite(x) and x>0
def on_frame_grid(x, fps): return finite(x) and abs(x*fps-round(x*fps))<1e-6

def validate(m, root):
    errors=[]
    for k in ('project','revision','scene','route','render','clips','invariants','sources'):
        if k not in m: errors.append('Missing '+k)
    if errors: raise ValueError('; '.join(errors))
    for k in ('scene','route'):
        if not (root/m[k]).is_file(): errors.append('Missing file '+m[k])
    for k in ('fps','width','height','samples'):
        if not positive(m['render'].get(k)): errors.append('Invalid render '+k)
    for k in ('width','height','samples'):
        if positive(m['render'].get(k)) and int(m['render'][k])!=m['render'][k]: errors.append(k+' must be integer')
    for k in ('width','height'):
        if positive(m['render'].get(k)) and m['render'][k]%2: errors.append(k+' must be even for yuv420p')
    if not m['sources']: errors.append('Provide spatial/appearance evidence')
    route=None
    if (root/m['route']).is_file():
        route=json.loads((root/m['route']).read_text())
        if route.get('coordinates')!='blender-z-up-metres': errors.append('Convert route explicitly to blender-z-up-metres')
        if not positive(route.get('fps')): errors.append('Invalid route fps')
        if not positive(route.get('duration')): errors.append('Invalid duration')
        if not 1<float(route.get('horizontal_fov',0))<179: errors.append('Invalid horizontal FOV')
        frames=route.get('frames',[])
        if len(frames)<2: errors.append('Need at least two camera samples')
        for i,f in enumerate(frames):
            if f.get('frame')!=i+1: errors.append('Camera samples must be contiguous from frame 1'); break
            for k in ('position','target'):
                v=f.get(k,[])
                if len(v)!=3 or not all(finite(x) for x in v): errors.append('Invalid '+k)
            if f.get('position')==f.get('target'): errors.append('Zero camera direction')
        if frames and positive(route.get('duration')) and positive(route.get('fps')):
            if abs((len(frames)-1)/route['fps']-route['duration'])>1e-6: errors.append('Route duration/sample count mismatch')
    end=0
    for c in m['clips']:
        start=c.get('start'); duration=c.get('duration')
        if not finite(start) or start<0 or not positive(duration):
            errors.append('Clip start must be finite and nonnegative; duration must be positive'); continue
        if abs(start-end)>1e-6: errors.append('Clips must be positive and contiguous')
        if positive(m['render'].get('fps')) and not all(on_frame_grid(v,m['render']['fps']) for v in (start,duration)):
            errors.append('Clip boundaries must align with rendered frames')
        end=start+duration
    if route and positive(route.get('duration')) and abs(end-route['duration'])>1e-6: errors.append('Clips do not cover route')
    if route and positive(route.get('duration')) and positive(m['render'].get('fps')):
        fps=m['render']['fps']
        if not on_frame_grid(route['duration'],fps): errors.append('Duration must contain an integer number of rendered frames')
        if positive(route.get('fps')) and round(route['duration']*fps)>1 and abs(route['fps']/fps-round(route['fps']/fps))>1e-6:
            errors.append('Render FPS must sample integer route frames; resample route first')
    if errors: raise ValueError('; '.join(errors))
    return route

def snapshot(root):
    root=Path(root).resolve()
    if not root.is_dir(): raise ValueError('Protected root must be an existing directory')
    files=sorted(root.rglob('*'))
    if any(p.is_symlink() for p in files): raise ValueError('Protected assets must not contain symbolic links')
    result={str(p.relative_to(root)):sha(p) for p in files if p.is_file()}
    if not result: raise ValueError('Protected directory contains no files')
    return result

def snapshot_paths(root,record):
    root=Path(root).resolve(); record=Path(record).resolve()
    if record==root or root in record.parents: raise ValueError('Store the hash record outside the protected directory')
    return root,record

def main():
    a=argparse.ArgumentParser(); sub=a.add_subparsers(dest='cmd',required=True)
    for name in ('validate','encode'):
        s=sub.add_parser(name); s.add_argument('manifest');
        if name=='encode': s.add_argument('frames'); s.add_argument('output')
    s=sub.add_parser('prompt'); s.add_argument('template'); s.add_argument('values'); s.add_argument('output')
    for name in ('snapshot','verify-assets'):
        s=sub.add_parser(name); s.add_argument('root'); s.add_argument('record')
    s=sub.add_parser('probe'); s.add_argument('video')
    s=sub.add_parser('assemble'); s.add_argument('config'); s.add_argument('output')
    x=a.parse_args()
    if x.cmd in ('validate','encode'):
        path=Path(x.manifest).resolve(); m=json.loads(path.read_text()); r=validate(m,path.parent)
        if x.cmd=='validate': print('Project inputs validated; spatial clearance still requires scene review.'); return
        out=Path(x.output); out.mkdir(parents=True,exist_ok=False)
        n=round(r['duration']*m['render']['fps']); frames=Path(x.frames).resolve()
        missing=[i for i in range(n) if not (frames/f'{i:06d}.png').is_file()]
        if missing: raise ValueError('Missing rendered frames: '+str(missing[:20]))
        full=out/'guide.mp4'
        run(['ffmpeg','-v','error','-n','-framerate',str(m['render']['fps']),'-i',str(frames/'%06d.png'),'-frames:v',str(n),'-c:v','libx264','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(full)])
        records=[]
        for i,c in enumerate(m['clips']):
            p=out/f'guide-{i+1:02d}.mp4'
            run(['ffmpeg','-v','error','-n','-ss',str(c['start']),'-i',str(full),'-t',str(c['duration']),'-an','-c:v','libx264','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(p)])
            records.append(dict(c,file=p.name,sha256=sha(p)))
        (out/'provenance.json').write_text(json.dumps({'project':m['project'],'revision':m['revision'],'scene_sha256':sha(path.parent/m['scene']),'route_sha256':sha(path.parent/m['route']),'clips':records},indent=2))
    elif x.cmd=='prompt':
        import re
        t=Path(x.template).read_text(); values=json.loads(Path(x.values).read_text())
        fields=set(re.findall(r'\{\{([a-z_]+)\}\}',t)); missing=fields-values.keys()
        if missing: raise ValueError('Missing prompt fields: '+', '.join(sorted(missing)))
        for k in fields:
            value=values[k]
            if value is None or not str(value).strip() or re.search(r'\bREPLACE\b|\{\{[^{}]+\}\}',str(value)):
                raise ValueError('Unfilled prompt value: '+k)
        t=re.sub(r'\{\{([a-z_]+)\}\}',lambda match:str(values[match[1]]),t)
        if '{{' in t or '}}' in t: raise ValueError('Unresolved prompt fields')
        with open(x.output,'x') as f: f.write(t)
    elif x.cmd=='snapshot':
        root,record=snapshot_paths(x.root,x.record); before=snapshot(root)
        with open(record,'x') as f: json.dump(before,f,indent=2)
    elif x.cmd=='verify-assets':
        root,record=snapshot_paths(x.root,x.record)
        before=json.loads(record.read_text()); after=snapshot(root)
        if not isinstance(before,dict) or not before: raise ValueError('Invalid or empty asset record')
        diff=[k for k in before.keys()|after.keys() if before.get(k)!=after.get(k)]
        if diff: raise ValueError('Protected assets changed: '+', '.join(sorted(diff)))
        print('Protected assets unchanged')
    elif x.cmd=='probe':
        run(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_name,width,height,avg_frame_rate,pix_fmt','-of','json',x.video])
        run(['ffmpeg','-v','error','-xerror','-i',x.video,'-f','null','-'])
    elif x.cmd=='assemble':
        if Path(x.output).exists() or Path(x.output).is_symlink(): raise FileExistsError('Output already exists: '+x.output)
        cfgpath=Path(x.config).resolve(); cfg=json.loads(cfgpath.read_text()); args=['ffmpeg','-v','error','-n']; filters=[]; labels=[]
        fps=cfg['fps']; w=cfg['width']; h=cfg['height']
        if not positive(fps) or not all(isinstance(v,int) and v>0 and v%2==0 for v in (w,h)): raise ValueError('Invalid encoding settings')
        for i,c in enumerate(cfg['clips']):
            if not positive(c['duration']) or not finite(c.get('start',0)) or c.get('start',0)<0: raise ValueError('Invalid trim')
            p=cfgpath.parent/c['file']
            info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(p)]))
            if c.get('start',0)+c['duration']>float(info['format']['duration'])+1/fps: raise ValueError('Trim exceeds clip')
            args+=['-i',str(p)]
            filters.append(f'[{i}:v]trim=start={c.get("start",0)}:duration={c["duration"]},setpts=PTS-STARTPTS,fps={fps},scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,setsar=1,format=yuv420p[v{i}]'); labels.append(f'[v{i}]')
        if not labels: raise ValueError('No clips')
        filters.append(''.join(labels)+f'concat=n={len(labels)}:v=1:a=0[out]')
        run(args+['-filter_complex',';'.join(filters),'-map','[out]','-an','-c:v','libx264','-crf',str(cfg.get('crf',18)),'-movflags','+faststart',x.output])
if __name__=='__main__': main()

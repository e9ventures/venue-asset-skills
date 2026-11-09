"""Exercise real FFmpeg assembly without client media or paid generation."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/finish-venue-film/scripts/pipeline.py'


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'FFmpeg and FFprobe required')
class MediaTests(unittest.TestCase):
    def test_assembly_duration_frames_decode_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for index, color in enumerate(('red', 'blue')):
                subprocess.run([
                    'ffmpeg', '-v', 'error', '-f', 'lavfi', '-i',
                    f'color=c={color}:s=320x180:r=12:d=1', '-c:v', 'libx264',
                    '-pix_fmt', 'yuv420p', str(root / f'{index}.mp4'),
                ], check=True, capture_output=True)
            config = {'fps': 12, 'width': 320, 'height': 180, 'clips': [
                {'file': f'{i}.mp4', 'start': 0, 'duration': 1} for i in range(2)
            ]}
            config_path = root / 'assembly.json'
            config_path.write_text(json.dumps(config))
            output = root / 'out.mp4'
            command = [sys.executable, str(SCRIPT), 'assemble', str(config_path), str(output)]
            subprocess.run(command, check=True, capture_output=True)
            subprocess.run([sys.executable, str(SCRIPT), 'probe', str(output)], check=True, capture_output=True)
            info = json.loads(subprocess.check_output([
                'ffprobe', '-v', 'error', '-count_frames', '-show_entries',
                'stream=codec_type,nb_read_frames:format=duration', '-of', 'json', str(output),
            ]))
            self.assertEqual(info['streams'], [{'codec_type': 'video', 'nb_read_frames': '24'}])
            self.assertEqual(float(info['format']['duration']), 2)
            original = output.read_bytes()
            retry = subprocess.run(command, capture_output=True)
            self.assertNotEqual(retry.returncode, 0)
            self.assertEqual(output.read_bytes(), original)

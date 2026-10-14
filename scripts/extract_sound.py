#!/usr/bin/env python
# -*- coding: utf-8 -*-

# extract sound from a video file, giving it correct extension


"""
Usage:
    {self_filename} [options] <file>
    {self_filename} -h | --help

Options:
    -s --audio-stream <n>        force audio stream [default: 0]
    -o --out <filename>          output filename (without extension) (default: <input_filename>)
"""


import re
import subprocess
import sys
from pathlib import Path

from docopt import docopt


def execute(command):
    process_output = subprocess.check_output(command, shell=True)
    try:
        cmnd_output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as exc:             # subprocess returned non 0 output code
        print("Status : FAIL", exc.returncode, exc.output)
    else:
        print("Output: \n{}\n".format(cmnd_output))
    return cmnd_output  # type: ignore

args = docopt(__doc__.format(self_filename=Path(__file__).name))
in_filepath = Path(args['<file>'])

# audio stream index to extract (from -s / --audio-stream)
try:
    audio_stream_index = int(args['--audio-stream'])
except (TypeError, ValueError):
    print("Error: --audio-stream must be an integer (got {!r})".format(args['--audio-stream']))
    sys.exit(1)

assert in_filepath.is_file(), "Input file does not exist: {}".format(in_filepath)

# get audio stream type
audio_format = execute(f'ffprobe -v error -select_streams a:{audio_stream_index} -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 "{in_filepath}"')
audio_format = audio_format.strip().decode("utf-8")
if audio_format == "":
    raise Exception("No audio found in file")
# get audio region code
audio_region = execute(f'ffprobe -v error -select_streams a:{audio_stream_index} -show_entries stream_tags=language -of default=noprint_wrappers=1:nokey=1 "{in_filepath}"')
audio_region = audio_region.strip().decode("utf-8")
print(f"-> audio_format: {audio_format} {"" if not audio_region else f'[{audio_region}]'}")

# WAV formats special case
if re.search('pcm_.*', audio_format):
    audio_format = "wav"

audio_region_str = f" - [{audio_region}]" if audio_region else ""
out_filepath = Path(f"{args['--out']}.{audio_format}") if args['--out'] else Path(f"{in_filepath.stem}{audio_region_str}.{audio_format}")

# Do the convertion, mapping the selected audio stream
command = 'nice -n 19 ffmpeg -i "{in_file}" -map 0:a:{stream} -c:a copy "{out_file}" -y'.format(
    in_file = in_filepath,
    stream = audio_stream_index,
    out_file = out_filepath
)
execute(command)

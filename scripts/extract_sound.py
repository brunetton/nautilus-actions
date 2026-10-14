#!/usr/bin/env python
# -*- coding: utf-8 -*-

# extract sound from a video file, giving it correct extension


"""
Usage:
    {self_filename} [options] <file>
    {self_filename} -h | --help

Options:
    -s --audio-stream <n>        force audio stream [default: 0]
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
print("-> audio_format: {}".format(audio_format))

# WAV formats special case
if re.search('pcm_.*', audio_format):
    audio_format = "wav"

out_filepath = in_filepath.with_suffix('.' + audio_format)

# Do the convertion, mapping the selected audio stream
command = 'ffmpeg -i "{in_file}" -map 0:a:{stream} -c:a copy "{out_file}" -y'.format(
    in_file = in_filepath,
    stream = audio_stream_index,
    out_file = out_filepath
)
execute(command)

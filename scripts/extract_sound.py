#!/usr/bin/env python
# -*- coding: utf-8 -*-

# extract sound from a video file, giving it correct extension

import os
import re
import subprocess
import sys

assert len(sys.argv) == 2

def execute(command):
    process_output = subprocess.check_output(command, shell=True)
    try:
        cmnd_output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as exc:             # subprocess returned non 0 output code
        print("Status : FAIL", exc.returncode, exc.output)
    else:
        print("Output: \n{}\n".format(cmnd_output))
    return cmnd_output  # type: ignore

in_complete_filename = sys.argv[1]
path = os.path.dirname(in_complete_filename)
in_filename_without_ext = os.path.splitext(os.path.basename(in_complete_filename))[0]

assert os.path.isfile(in_complete_filename)

# get audio stream type
audio_format = execute('ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 "{}"'.format(in_complete_filename))
audio_format = audio_format.strip().decode("utf-8")
if audio_format == "":
    raise Exception("No audio found in file")
print("-> audio_format: {}".format(audio_format))

# WAV formats special case
if re.search('pcm_.*', audio_format):
    audio_format = "wav"

# Do the convertion
command = 'ffmpeg -i "{in_file}" -c:a copy "{out_file}" -y'.format(
    in_file = in_complete_filename,
    out_file = os.path.join(path, in_filename_without_ext + '.' + audio_format)
)
execute(command)

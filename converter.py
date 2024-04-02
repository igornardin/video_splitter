from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_extract_audio
import pandas as pd

def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

input_file = pd.read_csv("input/input.csv")

for index, line in input_file.iterrows():
    ffmpeg_extract_subclip("input/{}".format(line["input_mp4"]), get_sec(line["begin"]), get_sec(line["end"]), targetname="output/{}_{}.mp4".format(line["prefix"], line["surname"]))
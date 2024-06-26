'''
This script converts audio, image, and video files to different formats using the PyDub, Pillow, and MoviePy libraries.

Neetre 2024
'''

from pydub import AudioSegment
from PIL import Image
from moviepy.editor import VideoFileClip
from pathlib import Path


def convert_audio(input_file, suffix="mp3", progress_bar=None):
    output_file = str(Path(input_file).with_suffix(f".{suffix}"))
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format=suffix)
    print(f"Converted {input_file} to {output_file}")


def convert_image(input_file, suffix=".png"):
    output_file = str(Path(input_file).with_suffix(f".{suffix}"))
    image = Image.open(input_file)
    image.save(output_file)
    print(f"Converted {input_file} to {output_file}")


def convert_video(input_file, suffix=".mp4", progress_bar=None):
    output_file = str(Path(input_file).with_suffix(f".{suffix}"))
    video = VideoFileClip(input_file)
    video.write_videofile(output_file, progress_bar=progress_bar)
    print(f"Converted {input_file} to {output_file}")


if __name__ == "__main__":
    convert_audio("../data/audio/input.wav", "../data/audio/output.mp3")
    convert_image("../data/image/input.jpg", "../data/image/output.png")
    convert_video("../data/video/input.avi", "../data/video/output.mp4")

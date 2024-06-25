'''
This script is used to convert the video file to the required format.

Neetre 2024
'''

from moviepy.editor import VideoFileClip

def convert_video(input_file, output_file):
    video = VideoFileClip(input_file)
    video.write_videofile(output_file)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    convert_video("../data/video/input.mp4", "../data/video/output.mp4")

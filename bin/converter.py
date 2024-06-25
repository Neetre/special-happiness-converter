from pydub import AudioSegment

def convert_audio(input_file, output_file, format="mp3"):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format=format)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    convert_audio("../data/audio/input.wav", "../data/audio/output.mp3")



from PIL import Image

def convert_image(input_file, output_file):
    image = Image.open(input_file)
    image.save(output_file)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    convert_image("../data/image/input.jpg", "../data/image/output.png")


from moviepy.editor import VideoFileClip

def convert_video(input_file, output_file):
    video = VideoFileClip(input_file)
    video.write_videofile(output_file)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    convert_video("../data/video/input.avi", "../data/video/output.mp4")
'''
This script is used to convert audio files from one format to another.

Neetre 2024
'''

from pydub import AudioSegment

def convert_audio(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="mp3")
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    convert_audio("../data/audio/input.wav", "../data/audio/output.mp3")

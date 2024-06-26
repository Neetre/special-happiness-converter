'''
This is the main file for the router. It will be responsible for routing the requests to the appropriate scripts.

Neetre 2024
'''

import argparse
from icecream import ic

from converter import convert_image, convert_audio, convert_video
from gui import gui


def args_parse():
    parser = argparse.ArgumentParser(description="Convert files to different formats")
    parser.add_argument("--cli", action="store_true", help="Run the program in CLI mode")
    parser.add_argument("--gui", action="store_true", help="Run the program in GUI mode")
    parser.add_argument("--type", type=str, help="Type of file (image, audio, video)")
    parser.add_argument("-in", "--input", type=str, help="Input file path")
    parser.add_argument("-s", "--suffix", type=str, help="Output file suffix")
    # parser.add_argument("-out", "--output", type=str, help="Output file path")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    return parser.parse_args()


def main():
    args = args_parse()
    ic(args)
    
    if args.gui:
        gui()

    if args.cli:
    
        if args.type == "image":
            suffix = args.suffix if args.suffix else ".png"
            convert_image(args.input, suffix)
        elif args.type == "audio":
            suffix = args.suffix if args.suffix else ".mp3"
            convert_audio(args.input, suffix)
        elif args.type == "video":
            suffix = args.suffix if args.suffix else ".mp4"
            convert_video(args.input, suffix)
        else:
            print("Invalid type of file. Please provide image, audio, or video.")
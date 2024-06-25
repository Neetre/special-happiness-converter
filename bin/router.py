'''
This is the main file for the router. It will be responsible for routing the requests to the appropriate scripts.

Neetre 2024
'''

import argparse
from icecream import ic

from converter import convert_image, convert_audio, convert_video


def args_parse():
    parser = argparse.ArgumentParser(description="Convert files to different formats")
    parser.add_argument("--type", type=str, help="Type of file (image, audio, video)")
    parser.add_argument("--input-ext", type=str, help="Input file extension")
    parser.add_argument("--output-ext", type=str, help="Output file extension")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    return parser.parse_args()


def main():
    args = args_parse()
    ic(args)
    if args.type == "image":
        convert_image(args.input, args.output)
    elif args.type == "audio":
        convert_audio(args.input, args.output)
    elif args.type == "video":
        convert_video(args.input, args.output)
    else:
        print("Invalid type of file. Please provide image, audio, or video.")
'''
This is the main file for the router. It will be responsible for routing the requests to the appropriate scripts.

Neetre 2024
'''

import argparse
from icecream import ic

from converter import convert_image, convert_audio, convert_video
from gui_custom import gui_


video_extensions = ['mp4', 'avi', 'mov', 'mkv']
audio_extensions = ['mp3', 'wav', 'flac']
image_extensions = ['png', 'jpg', 'jpeg', 'heic']


def args_parse():
    parser = argparse.ArgumentParser(description="Convert files to different formats")
    parser.add_argument("--cli", action="store_true", help="Run the program in CLI mode")
    parser.add_argument("--gui", action="store_true", help="Run the program in GUI mode")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Increase output verbosity")
    return parser.parse_args()


def main():
    args = args_parse()

    if args.verbose:
        ic.enable()
    else:
        ic.disable()
    
    if args.gui:
        gui_()

    elif args.cli:
        
        while True:
            input_file = input("Enter the path to the file you want to convert (read the readme for suggestions): ")
            input_file = "../" + input_file.strip()
            tipe = input("Enter the type of file you want to convert (video, audio, image): ")
            tipe = tipe.lower().strip()
            output_format = input("Enter the output format (mp3, mp4, png, ...): ")
            output_format = output_format.lower().strip()

            if not input_file:
                print("Please select a file.")
                continue

            try:
                if tipe == "video":
                    convert_video(input_file, output_format)
                elif tipe == "audio":
                    convert_audio(input_file, output_format)
                elif tipe == "image":
                    convert_image(input_file, output_format)

                print("Conversion completed successfully.")
            
            except Exception as e:
                print(f"Conversion failed: {str(e)}")
                
            q = input("Do you want to convert another file? (y/n): ")
            if q.lower() != "y":
                break

    else:
        print("Please specify either --cli or --gui")


if __name__ == "__main__":
    main()
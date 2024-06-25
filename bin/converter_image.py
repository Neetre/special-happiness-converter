'''
The script is used to convert the image to the required format.

Neetre 2024
'''

from PIL import Image

def convert_image(input_file, output_file):
    image = Image.open(input_file)
    image.save(output_file)
    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    convert_image("../data/image/input.jpg", "../data/image/output.png")
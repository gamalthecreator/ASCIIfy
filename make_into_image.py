from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog
import os


# open image using a file chooser dialog
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    return file_path


def create_ascii_image(ascii_text, font_size, image_output_path):
    # Set padding for the image
    padding = 10

    # Calculate the image size based on font size and text length
    max_line_length = max(len(line) for line in ascii_text)
    text_width = (max_line_length ) * font_size // 2 + (2 * padding)
    text_height = (len(ascii_text) * font_size) + (2 * padding)

    # Create a new image with baby blue background (173, 216, 230)
    image = Image.new("RGB", (text_width, text_height), color = "white")
    draw = ImageDraw.Draw(image)

    # Use a generic font (Pillow's built-in fonts)
    font = ImageFont.load_default()  # Load a generic font (Pillow's built-in default font)

    # Set the text color (black) and background color (white)
    text_color = "black"
    background_color = "white"

    # Write the ASCII text on the image, make it bold
    for i, line in enumerate(ascii_text):
        bbox = draw.textbbox((0, 0), line, font=font)
        x = (text_width - (bbox[2] - bbox[0])) / 2
        y = padding + i * font_size
        draw.text((x, y), line, fill=text_color, font=font)

    # Save the image
    image.save(image_output_path)

def main():
    # Load your ASCII characters from the text file
    file_path = open_file_dialog()
    with open(file_path, "r") as file:
        ascii_text = file.readlines()

    # Set the font size for the ASCII art image
    font_size = 10  # Adjust the font size as needed

    # Specify the output path and format for the image
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    image_output_path = file_name + "output_image.png"  # Replace with the desired output image path and format

    create_ascii_image(ascii_text, font_size, image_output_path)

if __name__ == "__main__":
    main()
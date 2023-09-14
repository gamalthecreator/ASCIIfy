from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

ascii_chars = '@&B9#SGHM352Xsr;:,. '  #Define the ASCII chars from darker to brighter
# ascii_chars = '@%#*+=-:. '  #Define the ASCII chars from darker to brighter

# open image using a file chooser dialog
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    return file_path

#show a prompt that asks you to open the file or not
def show_prompt():
    root = tk.Tk()
    root.withdraw()
    answer = tk.messagebox.askyesno("Open file", "Do you want to open the file?")
    if answer:
        openASCIIArtFile()
    else:
        print("Thanks for using ASCIIfy!")
    root.destroy()

#open the file if you choose to

def openASCIIArtFile():
    try:
        os.startfile(output_path)
    except:
        pass
    print("No file to open.")


# Resize the image to desired width while maintaining aspect ratio
def resize(image):
    width = 150
    height = int((width / float(image.width)) * image.height)
    # height = int((width * float(image.height) ) / image.width)
    image = image.resize((width, height))
    return image, width, height

# Convert the image to grayscale
def graify(image):
    image = image.convert('L')
    return image

# Generate ASCII art with dithering
def getASCII(image, width, height):
    ascii_art = ''
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            char_index = int(pixel / 255 * (len(ascii_chars) - 1))
            ascii_art += ascii_chars[char_index] * 2  # Use the same character twice for better aspect ratio
        ascii_art += '\n'
    return ascii_art

# Save the ASCII art to a text file
def saveToFile(ascii_art):
    file_name = os.path.splitext(os.path.basename(image_path))[0]
    output_file = file_name + '_ascii_art.txt'
    with open(output_file, 'w') as file:
        file.write(ascii_art)

    print(f'ASCII art saved to {output_file}.')
    return output_file

# Load the image
image_path = open_file_dialog()
image = Image.open(image_path)
image, width, height = resize(image)
image = graify(image)
ascii_art = getASCII(image, width, height)
output_path = saveToFile(ascii_art)
show_prompt()


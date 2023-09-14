# ASCIIfy
# ASCII Art Generator and ASCII Image Converter README

## Introduction
The ASCII Art Generator is a Python program that converts images into ASCII art text representations. It utilizes the Python Imaging Library (PIL) for image manipulation and tkinter for creating a simple graphical user interface (GUI). This program allows you to convert your favorite images into ASCII art and save them as text files.

Additionally, there is another program file named "make_into_image.py" that can be used to convert the generated ASCII art text file back into an image.

## How to Use ASCII Art Generator
1. Run the `ascii_art_generator.py` script using Python (Python 3.x is recommended).

2. The program will open a file dialog prompting you to select an image (JPEG format is preferred).

3. Once you've selected an image, the program will resize it while maintaining its aspect ratio to a width of 60 characters.

4. The image will be converted to grayscale for better representation as ASCII art.

5. The program then generates ASCII art by mapping pixel brightness to predefined ASCII characters.

6. The generated ASCII art will be saved as a text file with the same name as the input image but with '_ascii_art.txt' appended.

7. You will be prompted whether you want to open the generated ASCII art text file.

## Using make_into_image.py
1. Run the `make_into_image.py` script using Python (Python 3.x is recommended).

2. The program will open a file dialog prompting you to select an ASCII art text file (generated using the ASCII Art Generator).

3. The program will convert the ASCII art text back into an image representation.

4. The generated image will be saved in the same directory as the selected ASCII art text file.

## Additional Options
- You can modify the `ascii_chars` variable in the `ascii_art_generator.py` script to control the characters used in the ASCII representation. Darker characters should be placed at the beginning of the string, and lighter characters towards the end.

## Requirements
- Python 3.x
- Python Imaging Library (PIL)
- tkinter (usually included with Python installations)

## Usage Example
1. Run the `ascii_art_generator.py` script to generate ASCII art.

2. Run the `make_into_image.py` script to convert the generated ASCII art back into an image.

## Notes
- The generated ASCII art might look better in monospaced fonts.

- Experiment with different input images and ASCII characters to achieve varied results.

- These programs are intended for educational and entertainment purposes.

## Contact
If you have any questions or suggestions, feel free to contact me at s-gamal.shehata@zewailcity.edu.eg

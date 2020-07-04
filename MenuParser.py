# Written by Alex Deok-Hwan Kim (Arta)
# This personal project is dedicated to making my parents' lives a lot better by automation.

# MenuParser takes a picture of a restaurant menu, recognizes text, and parses it to come up
# with a JSON file that contains the menu item name and its price.
# It uses Tesseract for OCR and OpenCV for image handling.

import pytesseract
import cv2 as cv
import sys
from os import path
from util import cvhandler, npparser as np
import argparse

# First and foremost: letting PyTesseract recognize the path for Tesseract
try:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
    # Argument parser to help with arguments
    parser = argparse.ArgumentParser()

    # Sometimes greyscaling and denoising help with better text recognition from Tesseract.
    # But, sometimes raw is better.
    parser.add_argument("image", help="Sets image input path")
    parser.add_argument("-g", "--greyscale", action="store_true", help="Uses OpenCV Greyscaling")
    parser.add_argument("-d", "--denoise", action="store_true", help="Uses OpenCV Denoising")
    parser.add_argument("--output", required=True, help="Sets output file name")
    args = parser.parse_args()
    if not path.exists(args.image):
        raise FileNotFoundError
    image = cv.imread(args.image)  # Loading the image passed through the argument to OpenCV

    # This block of code handles the first text recognition from TesseracSt and store it into a txt file.
    # The output path is determined by the argument, and it creates a new file or overwrites the existing file.
    with open(f"output\{args.output}", "w", encoding="utf8") as text_file:
        if args.denoise:
            image = cvhandler.denoise(image)  # Special handler for denoise and greyscale.
            print(f"\n*** \"{args.image}\" has been denoised")
        if args.greyscale:
            image = cvhandler.greyscale(image)
            print(f"\n*** \"{args.image}\" has been greyscaled")
        text_file.write(pytesseract.image_to_string(image))
        print(f"\n*** Successfully extracted text from \"{args.image}\" to \"{args.output}\" in the output folder")
    # This block of code handles the conversion of .txt file to .JSON file.
    # JSON file is mostly for the quality of life aspect, sometimes looking at the raw .txt helps more than .JSON
    # Entirely up to the user whether to look at the .txt or .JSON, but definitely compare both to see the better fit.
    with open(f"output\{args.output}_parsed.JSON", "w", encoding="utf8") as parsed_file:
        print(f"\n*** Parsing {args.output}. . .")
        parsed_file.write(np.npparse(f"output\{args.output}"))
        print(f"\n*** Successfully parsed \"{args.output}\" into \"{args.output}_parsed.JSON\"\n")
except FileNotFoundError:
    print(f"Image at file path \"{path.realpath(args.image)}\" does not exist.")
    sys.exit(1)
except TypeError:
    print(f"Image file \"{path.realpath(args.image)}\" is not a valid image file.")
    sys.exit(1)


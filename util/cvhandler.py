# Written by Alex Deok-Hwan Kim (Arta)
# This personal project is dedicated to making my parents' lives a lot better by automation.

# cvhandler handles the image manipulation part. There are only two for now, but more can be added down the line.

import cv2 as cv  # Just a quality of life change from cv2 to cv


def greyscale(image):  # As mentioned before, sometimes greyscaling helps, sometimes it doesn't.
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


def denoise(image):  # Denoising is generally more effective than greyscaling, but still unreliable.
    # The params are:
    # (InputArray, OutputArray, FilterStrength, ColorFilterStrength, TemplateWindowSize, SearchWindowSize)
    # Higher FilterStrength and ColorFilterStrength numbers reduce more noise, but image detail might suffer.
    # I figured 10 was a decent number that is both generating good results and not degrading the image quality.
    # TemplateWindowSize and SearchWindowSize are recommended to be 7 and 21 respectively.
    dst = cv.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    return dst

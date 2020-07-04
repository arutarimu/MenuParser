# MenuParser
## Introduction
MenuParser is an restaurant menu parser using Tesseract and OpenCV written in Python 3. It takes in a picture or a photo of a restaurant menu, and spits out a text file and a JSON file with the item name and price.  
This is achieved by utilizing Tesseract Optical Character Recognition technology, along with OpenCV's image manipulation.

## Usage
Unfortunately, it can only be used on a small chunk of the menu at a time. It also can't be used on poor quality pictures or photos, because of the OCR technology limitations. 
* _First_, you need to make sure the image is parsable. A region of the menu must be chunked out and rows should be distinct.  
For example, you *have* to chunk the region like this:  
`Something Delicious        1.99`  
`Something Really Delicious 13.99`  
`Coke or something similar  1.00`  
It does not have to have aligned columns.  
What **not** to do:
`Something Delicious   1.99   Something Really Delicious 13.99`
* _Second_, make sure to have your image file within the same directory as the main folder, and run like this.  
 `MenuParser.py [image_file] --output [destination_file]`  
 This runs the raw picture without any image manipulation. See if this works out well. If not, proceed.  
 There are arguments which can help with the OCR accuracy: **denoise** and **greyscale**.  
 **Denoise** reduces the grainy pixels on digitally degraded images. These griany pixels confuse the OCR algorithm, and causes inaccuracy.  
 **Greyscale** changes the image to black and white, thus easier to recognize text.  
 These features don't *always* grant better results. Please use best judgement after playing around with the settings.  
 **Denoise**: `-d, --denoise` ie: `MenuParser.py [image_file] --output [destination_file.txt] -d`  
 **Greyscale**: `-g, --greyscale` ie: `MenuParser.py [image_file] --output [destination_file] -g` 
 * _Third_, you will have two files in `output` folder: `[destination_file.txt]` and `[destination_file.txt]_parsed.JSON`  
 The JSON file is very easy to work with, but do check the .txt file as well for more accuracy.  
 
## Parsing in Action

**1. Here is the initial test menu chunk. It only works if the chunk is like this:**  

  ![Test.png](https://i.imgur.com/5ghcDmD.png)  
  
**2. Run the program**  

  ![shell.png](https://i.imgur.com/9zCFNz5.png)  
  
**3. The initial text file from Optical Character Recognition**  

  ![ocr.png](https://i.imgur.com/s0jW2kV.png)  
  
**4. JSON parsing done through the program**  

![json.png](https://i.imgur.com/1TZeqke.png)  

### As you can see, the OCR is far from perfect. You *will* have to do some tweaking before copying and pasting. However, this is far better than having to manually input letter by letter.

## Requirements

- **Python 3.6.5** or higher
- **Tesseract 3.x** or higher for Linux, **Tesseract 5.0** for Windows
- **pytesseract** 0.3.4
- **opencv-python** 4.2.0.34 
## Roadmap

I plan on adding more features and better optimization down the line. But the most important thing I need to implement as of now is catching all the exceptions.  
These codes *don't* catch any exceptions now, so you will encounter some errors thrown in your way. I will actively add exceptions as time allows.

# Written by Alex Deok-Hwan Kim (Arta)
# This personal project is dedicated to making my parents' lives a lot better by automation.

# npparser parses name and price out of a raw .txt file spit out by Tesseract.
# It iterates through each line of .txt file, searches for a figure that could match the price, using RegEx.
# It then puts together the name and price, making a dictionary, then the dictionary is turned into a JSON format.

import re
import json


def npparse(file):  # Name and price parser that uses for-loop to find the match
    with open(file, "r", encoding="utf8") as text_file:
        np_dict = {}
        for line in text_file:
            np_item = match(line)
            if np_item != 0:  # if match(line) returns a non-zero value, it knows it is matched.
                name = np_item[0]  # match(line) returns two values, in a list.
                price = np_item[1]
                np_dict[name] = price
        return json_parse(np_dict)  # calls json_parse function to convert the dictionary into JSON.


def match(line):  # This function is the heavy lifter for parsing. It uses RegEx to match with the "price".
    words = line.split()
    name, price, i = "", "", 0  # i is used to track of iteration number
    for word in words:
        if re.match(r"^\d+([\,\.]\d\d)$", word):  # this RegEx only finds 9.99, 99.99, 999.99 ... so forth.
            price = words[i]  # the iteration number must be the index since RegEx got a hit.
            return name, price  # returns name and price, both at the same time in a list.
        name = name + word + " "
        i += 1
    return 0  # if it did not pass RegEx, return a zero value.


def json_parse(dictionary):  # a simple json parser
    json_dump = json.dumps(dictionary)
    return json_dump

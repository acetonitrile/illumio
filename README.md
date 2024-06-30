# Word Matcher

A Python script that finds matches of predefined words in an input file.

## Usage
python matcher.py <input_file> <predefined_words_file>

## Requirements

- Python 3 (any recent version from the last few years should work)
- No additional dependencies required

## Features
The matcher will read in the input file line by line, while chunking the line into megabyte pieces if necessary to handle extremely long lines.

Matcher does not indicate if there were multiple vs single match of the same word in a single line


## Tests

Expected output of python matcher.py input predefined_words
```
Word: abc
Found on lines: 2, 3

Word: efgh
Found on lines: 6, 7, 8
```
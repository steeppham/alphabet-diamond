#!/usr/bin/python
# Prints a diamond given an input letter.
# Usage: alphabet-pyramid.py <letter>
# -- letter 	The input letter that is a character between [a-zA-Z]

import sys
import string
import re

# check for valid input is [a-zA-Z]
if len(sys.argv) < 2:
	print "INVALID INPUT"
	sys.exit()
letter = sys.argv[1].upper()
if ord(letter) < ord('A') or ord(letter) > ord('Z'):
	print "INVALID INPUT"
	sys.exit()

# create the alphabet list up to the the input letter
# such that it is a palindrome
index = ord(letter) - ord('A')
alphabet = list(string.uppercase[:index + 1])
if index > 0:
	alphabet += alphabet[index-1::-1]

# print the diamond line by line using the alphabet list
for a in alphabet:
	pos = ord(a) - ord('A')
	# pre padding from the left
	line = ' ' * (index - pos)
	# the letter
	line += a
	# post padding up to the middle
	line += ' ' * pos
	# mirror the line for the right side
	if index > 0:
		line += line[index-1::-1]
	print line
# Shokunin - Alphabet Diamond

## The Challenge
Write a program which draws a diamond of the form illustrated below. The letter which is to appear at the widest point of the figure (E in the example) is to be specified as input data (CLI arg, keyboard read-in, etc).

                      A

                     B B

                    C   C

                   D     D

                  E       E

                   D     D

                    C   C

                     B B

                      A

Inputs are [a-zA-Z] (e.g. letters only, upper or lower case). Output is upper case only.
Edge cases:
If you input "a" or "A", then he output is simply "A".
If the input is invalid, then the output is "INVALID INPUT". If you read from keyboard input you may ask the user for a new input.

## How to Run

`./go.sh alphabet-pyramind.py [letter]`

The go script accepts an optional letter [a-zA-z] argument which will be used to print out the diamond. When no argument is specified the default letter 'E' will used instead.

If an invalid input is detected the program will output "INVALID INPUT" and exit.
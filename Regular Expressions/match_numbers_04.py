# Write a program that finds all integer and floating-point numbers in a string.

# A number has the following characteristics:
# •	Has either whitespace before it or the start of the string (match either ^ or what's called a positive lookbehind).
# •	The number might or might not be negative, so it might have a hyphen on its left side ("-").
# •	It consists of one or more digits.
# •	Might or might not have digits after the decimal point
# •	The decimal part (if it exists) consists of a period (".") and one or more digits after it. Use a capturing group.
# •	Has either whitespace before it or the end of the string (match either $ or what's called a positive lookahead).

import re

number = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, number)

for match in matches:
    print(match.group(), end=" ")

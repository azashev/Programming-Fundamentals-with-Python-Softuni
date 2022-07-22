# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.

import re

strings = input()

pattern = r"\d+"

while strings:
    matches = re.findall(pattern, strings)
    if matches:
        print(' '.join(matches), end=" ")

    strings = input()

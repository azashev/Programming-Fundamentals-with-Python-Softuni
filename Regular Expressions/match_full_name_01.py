# Write a program to match full names from a sequence of characters and print them on the console.

# First, write a regular expression to match a valid full name, according to these conditions:
# • A valid full name has the following characteristics:
#   - It consists of two words.
#   - Each word starts with a capital letter.
#   - After the first letter, it only contains lowercase letters.
#   - Each of the two words should be at least two letters long.
#   - A single space separates the two words.

import re

names = input()

pattern = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"

matches = re.findall(pattern, names)

print(" ".join(matches))

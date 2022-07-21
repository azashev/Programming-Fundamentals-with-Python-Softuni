# Write a regular expression to match a valid phone number from Sofia. After you find all valid phones, print them on
# the console, separated by a comma and a space ", ".


# A valid number has the following characteristics:
# • It starts with "+359"
# • Then, it is followed by the area code (always 2)
# • After that, it is followed by a number:
#   - The number consists of 7 digits (separated into two groups of 3 and 4 digits, respectively).
# • The different parts are separated by either a space or a hyphen ('-').


# First solution:

import re

text = input()

pattern = r"(\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b)"

matches = re.findall(pattern, text)

print(", ".join(matches))



# Second solution:

# import re
#
# text = input()
#
# matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)
#
# result = []
#
# for x in matches:
#     result.append(x.group())
#
# print(", ".join(result))

import re

string_input = input()

pattern = r"(:{2}([A-Z][a-z]{2,}):{2})|(\*{2}([A-Z][a-z]{2,})\*{2})"

matches = re.finditer(pattern, string_input)
digits = re.findall("\\d", string_input)

threshold = 1
emojis = {}
emojis_counter = 0

for digit in digits:
    threshold *= int(digit)

print(f"Cool threshold: {threshold}")

for match in matches:
    match = match.group()
    word = ""
    ascii_value = 0
    emojis_counter += 1

    for char in match:
        if not char == ":" and not char == "*":
            word += char
            ascii_value += ord(char)
    if ascii_value >= threshold:
        emojis[match] = ascii_value

separator = "\n"
print(f"{emojis_counter} emojis found in the text. The cool ones are:\n{separator.join(emojis)}")


# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.
# The cool threshold could be a huge number, so be mindful.
#
# An emoji is valid when:
# • It is surrounded by 2 characters, either "::" or "**"
# • It is at least 3 characters long (without the surrounding symbols)
# • It starts with a capital letter
# • Continues with lowercase letters only
#
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
#
#
# You need to count all valid emojis in the text and calculate their coolness.
# The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji.
#
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
#
#
# You need to print the result of the cool threshold and, after that to take all emojis out of the text, count them and
# print only the cool ones on the console.
#
#
# Input:
# • On the single input, you will receive a piece of string.
#
# Output:
# • On the first line of the output, print the obtained Cool threshold in the format:
# "Cool threshold: {coolThresholdSum}"
# • On the following line, print the count of all emojis found in the text in format:
# "{countOfAllEmojis} emojis found in the text. The cool ones are:
# {cool emoji 1}
# {cool emoji 2}
# ...
# {cool emoji N}"
#
# Constraints:
# There will always be at least one digit in the text!

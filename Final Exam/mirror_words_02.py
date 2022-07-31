import re

pattern = r"(@([A-Za-z]{3,})@@([A-Za-z]{3,})@|#([A-Za-z]{3,})##([A-Za-z]{3,})#)"

words = input()

matches = re.finditer(pattern, words)

pairs = []

for match in matches:
    if "@" in match.group():
        match = match.group().strip("@")
        pairs.append(match.split("@@"))
    elif "#" in match.group():
        match = match.group().strip("#")
        pairs.append(match.split("##"))


if len(pairs):
    print(f"{len(pairs)} word pairs found!")
else:
    print("No word pairs found!")

mirror_words = []

for pair in pairs:
    if pair[0] == pair[1][::-1]:
        mirror_words.append(pair[0] + " <=> " + pair[1])

if len(mirror_words):
    print("The mirror words are:")
    print(*mirror_words, sep=", ")
else:
    print("No mirror words!")


# On the first line of the input, you will be given a text string.
# To win the competition, you have to find all hidden word pairs, read them, and mark the ones that are mirror images of
# each other.
#
# First, you have to extract the hidden word pairs. Hidden word pairs are:
# • Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# • At least 3 characters long each (without the surrounding symbols)
# • Made up of letters only
#
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a
# match, and you have to store them somewhere.
#
# Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
#
# • If you don`t find any valid pairs, print: "No word pairs found!"
# • If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# • If there are no mirror words, print: "No mirror words!"
# • If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
#
#
# Input / Constraints:
# • You will receive a string.
#
# Output:
# • Print the proper output messages in the proper cases as described in the problem description.
# • If there are pairs of mirror words, print them in the end, each pair separated by ", ".
# • Each pair of mirror word must be printed with " <=> " between the words.

import re

pattern = r"(@([A-Za-z]{3,})@@([A-Za-z]{3,})@|#([A-Za-z]{3,})##([A-Za-z]{3,})#)"

words = input()

matches = re.finditer(pattern, words)

pairs = []

for match in matches:
    # match.group()
    # word = ""
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
    # for mirror_word in mirror_words:
    print(*mirror_words, sep=", ")
else:
    print("No mirror words!")

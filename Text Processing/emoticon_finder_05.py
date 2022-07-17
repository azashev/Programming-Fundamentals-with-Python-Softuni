# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

some_string = input()

emoticons = []

for i in range(len(some_string)):
    if some_string[i] == ":":
        emoticons.append(":" + some_string[i + 1])

print('\n'.join(emoticons))

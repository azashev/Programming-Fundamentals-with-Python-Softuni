some_string = input()

emoticons = []

for i in range(len(some_string)):
    if some_string[i] == ":":
        emoticons.append(":" + some_string[i + 1])

print('\n'.join(emoticons))

string = input()

indexes = []

for char in range(len(string)):
    if string[char].isupper():
        indexes.append(char)

print(indexes)

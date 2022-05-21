words = ["sand", "water", "fish", "sun"]

string = input()

counter = 0

for word in words:
    if word in string.lower():
        counter += string.lower().count(word.lower())

print(counter)

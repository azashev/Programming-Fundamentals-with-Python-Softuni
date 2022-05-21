words = ["sand", "water", "fish", "sun"]

string = input()

counter = 0

for word in words:
    if word in string.lower():
        counter += string.lower().count(word)

print(counter)

# inp = str(input()).lower()
#
# counter = inp.count("water") + inp.count("fish") + inp.count("sun") + inp.count("sand")
#
# print(counter)

# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format: "{char} -> {occurrences}".

words = input().replace(" ", "")

my_dict = {}

for char in words:
    if char not in my_dict:
        my_dict[char] = 0
    my_dict[char] += 1

    #else:
    #    my_dict[char] += 1

for word, value in my_dict.items():
    print(f"{word} -> {value}")

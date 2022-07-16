# Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N times,
# where N is the length of the string.
# Print the final strings concatenated into one string.

list_of_strings = input().split()

for string in list_of_strings:
    print(string * len(string), end="")

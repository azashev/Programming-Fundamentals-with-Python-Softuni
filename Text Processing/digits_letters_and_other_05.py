# Write a program that receives a single string.
# On the first line, print all the digits found in the string.
# On the second line, print all the letters.
# On the third line, print all the other characters.

# There will always be at least one digit, one letter, and one other character.

def digits(string):
    result = ""
    for ch in string:
        if ch.isdigit():
            result += ch
    return int(result)


def letters(string):
    result = ""
    for ch in string:
        if ch.isalpha():
            result += ch
    return result


def other(string):
    result = ""
    for ch in string:
        if not ch.isdigit() and not ch.isalpha():
            result += ch
    return result


string_input = input()
print(digits(string_input))
print(letters(string_input))
print(other(string_input))

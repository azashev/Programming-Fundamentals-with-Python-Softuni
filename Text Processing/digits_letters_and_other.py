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

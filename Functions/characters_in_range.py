def chars_in_range(first_character, second_character):
    result = ''
    for character in range(ord(first_character) + 1, ord(second_character)):
        result += chr(character)

    return result


first_char = input()
second_char = input()

print(' '.join(chars_in_range(first_char, second_char)))

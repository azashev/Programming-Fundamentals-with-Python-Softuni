# Receive a string consisting of a number between two letters.
# For the given string, you should perform different mathematical operations to achieve a result:

# •	First, if the letter in front of the number is:
#   - Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
#   - Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)

# •	Next, if the letter after the number is:
#   - Uppercase: subtract its position from the resulting number (starting from 1)
#   - Lowercase: add its position to the resulting number (starting from 1)

# Do the same calculations to multiple strings and keep track of only the total sum of all results.


# Input:
# •	The input comes from the console as a single line, holding a sequence of strings
# •	Strings are separated by one or more white spaces
# •	The input data will always be valid. There is no need to check it explicitly

# Output:
# •	Print at the console a single number:
#   - The total sum of all processed numbers, formatted to the second decimal separator

# Constraints:
# •	The count of the strings will be in the range [1 … 10]
# •	The numbers between the letters will be integers in the range [1 … 2 147 483 647]
# •	Time limit: 0.3 sec. Memory limit: 16 MB


def position_in_alphabet(char):
    return ord(char) - 96


strings_input = [x.strip() for x in input().split()]
total_sum = 0


for string in strings_input:
    current_number = ""

    for ch in string:
        if ch.isdigit():
            current_number += ch

    current_number = int(current_number)

    if string[0].isupper():
        current_letter = string[0].lower()
        current_number = current_number / position_in_alphabet(current_letter)
    elif string[0].islower():
        current_letter = string[0]
        current_number = current_number * position_in_alphabet(current_letter)

    if string[-1].isupper():
        current_letter = string[-1].lower()
        current_number -= position_in_alphabet(current_letter)
    elif string[-1].islower():
        current_letter = string[-1]
        current_number += position_in_alphabet(current_letter)

    total_sum += current_number

print(f"{total_sum:.2f}")

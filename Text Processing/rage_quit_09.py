string_input = input()

final_message = ""
symbols = ""
repeat_count = ""

for index in range(len(string_input)):
    if string_input[index].isdigit():
        if not index == len(string_input) - 1:
            if string_input[index + 1].isdigit():
                repeat_count += string_input[index]
            else:
                repeat_count += string_input[index]
                final_message += symbols * int(repeat_count)
                symbols = ""
                repeat_count = ""
        else:
            repeat_count += string_input[index]
            final_message += symbols * int(repeat_count)
            symbols = ""
            repeat_count = ""

    else:
        symbols += string_input[index].upper()

print(f"Unique symbols used: {len(set(final_message))}")

print(final_message)

# You'll be given a series of strings (containing only non-numerical characters) followed by non-negative
# numbers (N), e.g., "a3".
# Convert the letters to uppercase for each string and print it repeatedly N times on the console. In the example, you
# need to write back "AAA".

# First, on the output, print a statistic of the number of unique symbols used (case-insensitive) in the format:
# "Unique symbols used {0}".

# Next, print the rage message itself.

# The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and
# for each string, there will be a corresponding number. The input will be given on a single line.

# Input:
# • The input data should be read from the console.
# • It consists of a single line holding a series of string-number sequences.
# • The input data will always be valid. There is no need to check it explicitly.

# Output:
# • The output should be printed on the console. It should consist of exactly two lines:
#   - On the first line, print the number of unique symbols used in the message in the format described above.
#   - On the second line, print the rage message.

# Constraints:
# • The count of string-number pairs will be in the range [1 … 20 000].
# • Each string will contain any character except digits. The length of each string will be in the range [1 … 20].
# • The repeat count for each string will be an integer in the range [0 … 20].
# • Allowed working time for your program: 0.3 seconds. Allowed memory: 64 MB.

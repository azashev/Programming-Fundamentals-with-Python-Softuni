# On the first line of the input, you will receive the encrypted message.
# After that, until the "Decode" command is given, you will be receiving strings with instructions for different
# operations that need to be performed upon the concealed message to interpret it and reveal its true content.
#
# There are several types of instructions, split by '|'
# • "Move {number of letters}":
#   - Moves the first n letters to the back of the string
# • "Insert {index} {value}":
#   - Inserts the given value before the given index in the string
# • "ChangeAll {substring} {replacement}":
#   - Changes all occurrences of the given substring with the replacement text
#
# Input / Constraints:
# • On the first line, you will receive a string with a message.
# • On the following lines, you will be receiving commands, split by '|' .
# Output:
# • After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"

message = input()

while True:
    command = input()
    if command == "Decode":
        break

    command = command.split("|")

    if command[0] == "Move":
        number_of_letters = int(command[1])
        letters = ""

        for i in range(number_of_letters):
            letters += message[i]
        message += letters
        message = message.replace(letters, "", 1)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]

        message = message[:index] + value + message[index:]
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]

        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")

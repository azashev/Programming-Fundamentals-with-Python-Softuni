concealed_message = input()

while True:
    command = input()

    if command == "Reveal":
        break

    command = command.split(":|:")

    if command[0] == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print("error")
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]

        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)

print(f"You have a new text message: {concealed_message}")


# On the first line of the input, you will receive the concealed message.
# After that, until the "Reveal" command is given, you will receive strings with instructions for different operations
# that need to be performed upon the concealed message to interpret it and reveal its actual content.
#
# There are several types of instructions, split by ":|:"
# • "InsertSpace:|:{index}":
#   - Inserts a single space at the given index. The given index will always be valid.
#
# • "Reverse:|:{substring}":
#   - If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
#   - If not, print "error".
#   - This operation should replace only the first occurrence of the substring if there are two or more occurrences.
#
# • "ChangeAll:|:{substring}:|:{replacement}":
#   - Changes all occurrences of the given substring with the replacement text.
#
#
# Input / Constraints:
# • On the first line, you will receive a string with a message.
# • On the following lines, you will be receiving commands, split by ":|:".
#
# Output:
# • After each set of instructions, print the resulting string.
# • After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"

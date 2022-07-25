some_string = input()
command = input()

new_password = some_string

while True:
    if command == "Done":
        break

    if command == "TakeOdd":
        new_password = ''.join([new_password[i] for i in range(len(new_password)) if i % 2 != 0])
        print(new_password)

    # Second solution:
    # if command == "TakeOdd":
    #     pwd = ""
    #     for i in range(len(new_password)):
    #         if i % 2 != 0:
    #             pwd += ''.join(new_password[i])
    #     new_password = pwd
    #     print(new_password)

    else:
        command = command.split()

        if command[0] == "Cut":
            index = int(command[1])
            length = int(command[2])

            if index + length <= len(new_password):
                substring_to_remove = new_password[index:index + length]
                if substring_to_remove in new_password:
                    new_password = new_password.replace(substring_to_remove, "", 1)
            print(new_password)
        elif command[0] == "Substitute":
            substring = command[1]
            substitute = command[2]

            if substring in new_password:
                new_password = new_password.replace(substring, substitute)
                print(new_password)
            else:
                print("Nothing to replace!")

    command = input()

print(f"Your password is: {new_password}")


# Write a password reset program that performs a series of commands upon a predefined string.
# First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with
# commands split by a single space. The commands will be the following:
#
# • "TakeOdd":
#   - Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
#
# • "Cut {index} {length}":
#   - Gets the substring with the given length starting from the given index from the password and removes its first
#   occurrence, then prints the password on the console.
#   - The given index and the length will always be valid.

# • "Substitute {substring} {substitute}":
#   - If the raw password contains the given substring, replaces all of its occurrences with the substitute text given
#   and prints the result.
#   - If it doesn't, prints "Nothing to replace!".
#
#
# Input:
# • You will be receiving strings until the "Done" command is given.
#
# Output:
# • After the "Done" command is received, print:
#   "Your password is: {password}"
#
# Constraints:
# • The indexes from the "Cut {index} {length}" command will always be valid.

string_input = input()

while True:
    command_input = input()
    if command_input == "End":
        break

    command = command_input.split()

    if command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        string_input = string_input.replace(char, replacement)
        print(string_input)
    elif command[0] == "Includes":
        substring = command[1]
        if substring in string_input:
            print("True")
        else:
            print("False")
    elif command[0] == "Start":
        substring = command[1]
        if string_input.startswith(substring):
            print("True")
        else:
            print("False")
    elif command[0] == "Lowercase":
        string_input = string_input.lower()
        print(string_input)
    elif command[0] == "FindIndex":
        char = command[1]
        for i in range(len(string_input) - 1, -1, -1):
            if string_input[i] == char:
                print(i)
                break
    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        string_input = string_input[:start_index] + string_input[start_index + count:]
        print(string_input)

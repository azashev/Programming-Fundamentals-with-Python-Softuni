activation_key = input()

while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        print(f"Your activation key is: {activation_key}")
        break

    if command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        up_or_low = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        if up_or_low == "Upper":
            substring = activation_key[start_index:end_index].upper()
            activation_key = activation_key[:start_index] + substring + activation_key[end_index:]
        else:
            substring = activation_key[start_index:end_index].lower()
            activation_key = activation_key[:start_index] + substring + activation_key[end_index:]
        print(activation_key)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = ''.join(activation_key[:start_index] + activation_key[end_index:])
        print(activation_key)

# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for different
# operations that need to be performed upon the raw activation key.
#
# There are several types of instructions, split by ">>>":
# • "Contains>>>{substring}":
#   - If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
#   - Otherwise, prints: "Substring not found!"
#
# • "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
#   - Change the substring between the given indices (the end index is exclusive) to upper or lower case and then print
#   the activation key.
#   - All given indexes will be valid.
#
# • "Slice>>>{startIndex}>>>{endIndex}":
#   - Delete the characters between the start and end indices (the end index is exclusive) and print the activation key.
#   - Both indices will be valid.
#
# Input:
# • The first line of the input will be a string consisting of letters and numbers only.
# • After the first line, until the "Generate" command is given, you will be receiving strings.
# Output:
# • After the "Generate" command is received, print:
#   - "Your activation key is: {activation key}"

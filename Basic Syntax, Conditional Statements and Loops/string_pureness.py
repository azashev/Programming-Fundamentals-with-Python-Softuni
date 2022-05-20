number_of_strings = int(input())

for string in range(number_of_strings):
    is_pure = True

    new_string = input()

    for char in new_string:
        if char == "," or char == "." or char == "_":
            is_pure = False
            break

    if is_pure:
        print(f"{new_string} is pure.")
    else:
        print(f"{new_string} is not pure!")

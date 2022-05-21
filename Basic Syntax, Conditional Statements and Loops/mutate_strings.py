first_string = input()
second_string = input()

current_string = ''
new_string = first_string

for i in range(len(first_string)):
    current_string = second_string[: i + 1] + first_string[i + 1:]
    if current_string != new_string:
        new_string = current_string
        print(new_string)

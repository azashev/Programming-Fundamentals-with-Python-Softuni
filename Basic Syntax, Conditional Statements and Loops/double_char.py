# string = input()
#
# new_string = ''
#
# while string != "End":
#     if string == "SoftUni":
#         string = input()
#         continue
#     new_string = ''
#     for char in string:
#         new_string += char * 2
#
#     print(new_string)
#     string = input()

while True:
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    for char in command:
        print(char * 2, end="")

    print()

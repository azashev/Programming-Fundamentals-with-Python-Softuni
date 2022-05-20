string = input()

new_string = ''

while string != "End":
    if string == "SoftUni":
        string = input()
        continue
    new_string = ''
    for char in string:
        new_string += char * 2

    print(new_string)
    string = input()

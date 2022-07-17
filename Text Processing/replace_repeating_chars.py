some_string = input()

new_string = ""

for i in range(len(some_string)):
    if i == 0:
        new_string += some_string[i]
        continue

    if not some_string[i] == some_string[i - 1]:
        new_string += some_string[i]
    else:
        continue

print(new_string)

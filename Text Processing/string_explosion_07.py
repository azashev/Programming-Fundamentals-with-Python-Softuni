some_string = input()

strength = 0

final_string = ""

for i in range(len(some_string)):
    if some_string[i] == ">":
        strength += int(some_string[i + 1])
        final_string += some_string[i]
        continue
    if strength > 0:
        strength -= 1
        continue
    else:
        final_string += some_string[i]

print(final_string)

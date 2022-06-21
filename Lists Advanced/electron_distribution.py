# Problem: fill shells until there are no more electrons left

# Rules:
# •	The maximum number of electrons in a shell can be 2 * n², where n is the position of a shell

# •	Start filling the shells from the first one at the first position

# •	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the next shell,
# and so on

number_of_electrons = int(input())
result = []

current_shell_position = 1

while True:
    current_shell_needed_electrons = 2 * current_shell_position**2

    if number_of_electrons >= current_shell_needed_electrons:
        number_of_electrons -= current_shell_needed_electrons
        result.append(current_shell_needed_electrons)
    else:
        if number_of_electrons > 0:
            result.append(number_of_electrons)
            break
        else:
            break

    current_shell_position += 1
print(result)

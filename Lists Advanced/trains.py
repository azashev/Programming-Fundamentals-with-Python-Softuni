number = int(input())

wagons = [0] * number
command = input()

while command != "End":
    current_command = command.split()
    action = current_command[0]

    if action == "add":
        value = int(current_command[1])
        wagons[-1] += value
    else:
        current_index = int(current_command[1])
        value = int(current_command[2])

        if action == "insert":
            wagons[current_index] += value
        else:
            wagons[current_index] -= value

    command = input()

print(wagons)

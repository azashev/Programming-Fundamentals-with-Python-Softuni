integers = list(map(int, input().split()))

command = input()

while not command == "end":
    command = command.split()
    action = command[0]

    if action == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        integers[first_index], integers[second_index] = integers[second_index], integers[first_index]
    elif action == "multiply":
        first_index = int(command[1])
        second_index = int(command[2])
        integers[first_index] *= integers[second_index]
    elif action == "decrease":
        for num in range(len(integers)):
            integers[num] -= 1
    command = input()

print(*integers, sep=', ')

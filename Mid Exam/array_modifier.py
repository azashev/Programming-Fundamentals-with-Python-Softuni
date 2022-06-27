# You will be given an array with integers, separated by spaces. Modify the elements after receiving the following
# commands: swap, multiply, decrease

integers = list(map(int, input().split()))

command = input()

while not command == "end":
    command = command.split()
    action = command[0]

    if action == "swap":
        # take two elements and swap their places
        first_index = int(command[1])
        second_index = int(command[2])
        integers[first_index], integers[second_index] = integers[second_index], integers[first_index]

    elif action == "multiply":
        # take the element at the 1st index and multiply it with the element at the 2nd index. Save the product at the
        # 1st index
        first_index = int(command[1])
        second_index = int(command[2])
        integers[first_index] *= integers[second_index]

    elif action == "decrease":
        # decrease all elements in the array with 1
        for num in range(len(integers)):
            integers[num] -= 1
    command = input()

print(*integers, sep=', ')

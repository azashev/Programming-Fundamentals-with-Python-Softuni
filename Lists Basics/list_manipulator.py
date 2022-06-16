from sys import maxsize as sys_maxsize

list_of_numbers = list(map(int, input().split()))

command = input()

while command != "end":
    current_command = command.split()
    current_action = current_command[0]

    # Splits the list after the given index and exchanges the places of the two resulting sub-lists
    # If the index is outside the boundaries of the list, print "Invalid index"
    # A negative index is considered invalid
    if current_action == "exchange":
        middle_index = int(current_command[1])
        if 0 <= middle_index < len(list_of_numbers):
            left_half = list_of_numbers[middle_index + 1::]
            right_half = list_of_numbers[:middle_index + 1]
            list_of_numbers = left_half + right_half
        else:
            print("Invalid index")

        # Returns the index of the max even/odd element
        # If there are two or more equal min/max elements, return the index of the rightmost one
        # If a min/max even/odd element cannot be found, print "No matches"
    elif current_action == "max":
        even_or_odd = current_command[1]
        if even_or_odd == "even":
            index_of_max_number = None
            max_num = - sys_maxsize
            for num in range(len(list_of_numbers)):
                if list_of_numbers[num] % 2 == 0 and list_of_numbers[num] >= max_num:
                    index_of_max_number = num
                    max_num = list_of_numbers[num]
            if index_of_max_number is not None:
                print(index_of_max_number)
            else:
                print("No matches")

        elif even_or_odd == "odd":
            index_of_max_number = None
            max_num = - sys_maxsize
            for num in range(len(list_of_numbers)):
                if list_of_numbers[num] % 2 != 0 and list_of_numbers[num] >= max_num:
                    index_of_max_number = num
                    max_num = list_of_numbers[num]
            if index_of_max_number is not None:
                print(index_of_max_number)
            else:
                print("No matches")

    elif current_action == "min":
        even_or_odd = current_command[1]
        if even_or_odd == "even":
            index_of_min_number = None
            min_num = sys_maxsize
            for num in range(len(list_of_numbers)):
                if list_of_numbers[num] % 2 == 0 and list_of_numbers[num] <= min_num:
                    index_of_min_number = num
                    min_num = list_of_numbers[num]
            if index_of_min_number is not None:
                print(index_of_min_number)
            else:
                print("No matches")

        elif even_or_odd == "odd":
            index_of_min_number = None
            min_num = sys_maxsize
            for num in range(len(list_of_numbers)):
                if list_of_numbers[num] % 2 != 0 and list_of_numbers[num] <= min_num:
                    index_of_min_number = num
                    min_num = list_of_numbers[num]
            if index_of_min_number is not None:
                print(index_of_min_number)
            else:
                print("No matches")

    # Returns the first/last count even/odd elements
    # If the count is greater than the list length, print "Invalid count"
    # If there are not enough elements to satisfy the count, print as many as possible. If there are zero even/odd elements, print an empty list
    elif current_action == "first":
        current_count = int(current_command[1])
        even_or_odd = current_command[2]
        current_list = []

        if current_count <= len(list_of_numbers):
            if even_or_odd == "even":
                for num in list_of_numbers:
                    if num % 2 == 0:
                        current_list.append(num)
                    if len(current_list) > current_count:
                        current_list.pop()
                print(current_list)
            elif even_or_odd == "odd":
                for num in list_of_numbers:
                    if num % 2 != 0:
                        current_list.append(num)
                    if len(current_list) > current_count:
                        current_list.pop()
                print(current_list)
        else:
            print("Invalid count")

    elif current_action == "last":
        current_count = int(current_command[1])
        even_or_odd = current_command[2]
        current_list = []

        if current_count <= len(list_of_numbers):
            if even_or_odd == "even":
                for num in list_of_numbers:
                    if num % 2 == 0:
                        current_list.append(num)
                    if len(current_list) > current_count:
                        current_list.pop(0)
                print(current_list)
            elif even_or_odd == "odd":
                for num in list_of_numbers:
                    if num % 2 != 0:
                        current_list.append(num)
                    if len(current_list) > current_count:
                        current_list.pop(0)
                print(current_list)

        else:
            print("Invalid count")
    command = input()

print(list_of_numbers)

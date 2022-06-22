def increase_decrease(items, value):
    # increase the value of all elements in the sequence which are less or equal to the removed element with the value
    # of the removed element
    for x in range(len(items)):
        if items[x] <= value:
            items[x] += value
        else:
            items[x] -= value
    return items


input_list = list(map(int, input().split()))
total_sum = 0

while input_list:
    # When an index is received, remove the element at that index from the sequence
    current_index = int(input())

    # If the given index is less than 0, remove the first element of the sequence and copy the last element to its place
    # the elements must still be increased and decreased
    if current_index < 0:
        current_element_value = input_list.pop(0)
        total_sum += current_element_value
        input_list.insert(0, input_list[-1])
        input_list = increase_decrease(input_list, current_element_value)

    # If the given index is greater than the last index of the sequence, remove the last element from the sequence, and
    # copy the first element to its place
    # the elements must still be increased and decreased
    elif current_index >= len(input_list):
        current_element_value = input_list.pop(-1)
        total_sum += current_element_value
        input_list.append(input_list[0])
        input_list = increase_decrease(input_list, current_element_value)
    else:
        current_element_value = input_list.pop(current_index)
        total_sum += current_element_value
        input_list = increase_decrease(input_list, current_element_value)

print(total_sum)

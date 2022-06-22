def increase_decrease(items, value):
    for x in range(len(items)):
        if items[x] <= value:
            items[x] += value
        else:
            items[x] -= value
    return items


input_list = list(map(int, input().split()))
total_sum = 0

while input_list:
    current_index = int(input())
    if current_index < 0:
        current_element_value = input_list.pop(0)
        total_sum += current_element_value
        input_list.insert(0, input_list[-1])
        input_list = increase_decrease(input_list, current_element_value)
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

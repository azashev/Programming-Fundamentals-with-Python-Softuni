shuffle_list = input().split()
shuffles = int(input())

for shuffles in range(shuffles):
    left_half = shuffle_list[:(len(shuffle_list) // 2):]
    right_half = shuffle_list[(len(shuffle_list) // 2)::]
    current_list = []

    for i in range(len(shuffle_list) // 2):
        current_list.append(left_half[i])
        current_list.append(right_half[i])
    string = current_list

print(shuffle_list)

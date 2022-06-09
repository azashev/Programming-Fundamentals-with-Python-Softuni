string = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    left_half = string[:(len(string) // 2):]
    right_half = string[(len(string) // 2)::]
    current_list = []

    for i in range(len(string) // 2):
        current_list.append(left_half[i])
        current_list.append(right_half[i])
    string = current_list

print(string)

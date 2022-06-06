# first_list = []
#
# tail = first_list.append(input())
# body = first_list.append(input())
# head = first_list.append(input())
#
# final_list = []
#
# for element in range(len(first_list) - 1, -1, -1):
#     final_list.append(first_list[element])
#
# print(final_list)

list = []

tail = list.append(input())
body = list.append(input())
head = list.append(input())

list[0], list[2] = list[2], list[0]

print(list)

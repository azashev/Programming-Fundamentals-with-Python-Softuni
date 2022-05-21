# number = int(input())
#
# new_number = ''
#
# max_num = -9223372036854775807
# last_num = -9223372036854775807
# nums = ''
# for num in str(number):
#     if int(num) > max_num:
#         max_num = int(num)
#         new_number = num + new_number
#     elif max_num > int(num) > last_num:
#         new_number = str(max_num) + num + nums
#     elif max_num > int(num) < last_num:
#         nums += num
#         new_number += nums
#
#     last_num = int(num)
#
# print(int(new_number))


numbers = [int(num) for num in input()]
sorted_list = sorted(numbers, reverse=True)
for num in sorted_list:
    print(num, end="")


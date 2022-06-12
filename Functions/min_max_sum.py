# solution 1
# print(f"The minimum number is {min(list(int(num) for num in input().split()))}\n"
#       f"The maximum number is {max(list(int(num) for num in input().split()))}\n"
#       f"The sum number is: {sum(list(int(num) for num in input().split()))}")


# solution 2
# numbers = list(map(int, input().split()))
#
# min_num = min(numbers)
# max_num = max(numbers)
# sum_num = sum(numbers)
#
# print(f"The minimum number is {min_num}")
# print(f"The maximum number is {max_num}")
# print(f"The sum number is: {sum_num}")


# solution 3
def min_num(numbers):
    result_min_num = 9223372036854775807
    for num in numbers:
        if num < result_min_num:
            result_min_num = num

    return result_min_num


def max_num(numbers):
    result_max_num = -922337203685477580
    for num in numbers:
        if num > result_max_num:
            result_max_num = num

    return result_max_num


def sum_num(numbers):
    result_sum_num = 0

    for num in numbers:
        result_sum_num += num

    return result_sum_num


numbers = list(map(int, input().split()))

print(f"The minimum number is {min_num(numbers)}")
print(f"The maximum number is {max_num(numbers)}")
print(f"The sum number is: {sum_num(numbers)}")

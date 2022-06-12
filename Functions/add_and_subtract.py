def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(first_number, second_number):
    return first_number - second_number


def add_and_subtract(first_num, second_num, subtract_num):
    result = subtract(sum_numbers(first_num, second_num), subtract_num)

    return result


input_first_number = int(input())
input_second_number = int(input())
input_subtract_number = int(input())

print(add_and_subtract(input_first_number, input_second_number, input_subtract_number))

def calculations(first_number, second_number, operator):
    result = None

    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number // second_number
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number

    return result


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calculations(first_num, second_num, input_operator))

def factorial_division(first_number, second_number):
    first_factorial = 1
    second_factorial = 1

    for x in range(first_number, 0, -1):
        first_factorial *= x

    for y in range(second_number, 0, -1):
        second_factorial *= y

    result = first_factorial / second_factorial

    return f"{result:.2f}"


input_first_number = int(input())
input_second_number = int(input())

print(factorial_division(input_first_number, input_second_number))

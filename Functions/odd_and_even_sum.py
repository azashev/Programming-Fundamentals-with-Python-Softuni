def sum_odd_and_even(number):
    odd_sum = 0
    even_sum = 0

    for i in number:
        if int(i) % 2 != 0:
            odd_sum += int(i)
        else:
            even_sum += int(i)
    return odd_sum, even_sum


input_number = input()

result_odd_sum, result_even_sum = sum_odd_and_even(input_number)

print(f"Odd sum = {result_odd_sum}, Even sum = {result_even_sum}")

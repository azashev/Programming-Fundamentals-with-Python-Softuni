def absolute_number(number):
    return abs(number)


numbers = list(map(float, input().split()))

absolute_numbers = []

for x in numbers:
    absolute_numbers.append(absolute_number(x))

print(absolute_numbers)

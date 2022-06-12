def rounding(number):
    return round(number)


numbers = list(map(float, input().split()))
rounded_numbers = []

for number in numbers:
    rounded_numbers.append(rounding(number))

print(rounded_numbers)

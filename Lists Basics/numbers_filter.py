n = int(input())

numbers = []
filtered_numbers = []

for number in range(n):
    numbers.append(int(input()))

command = input()

for n in numbers:
    if command == 'even':
        if n % 2 == 0:
            filtered_numbers.append(n)
    if command == 'odd':
        if n % 2 != 0:
            filtered_numbers.append(n)
    if command == 'negative':
        if n < 0:
            filtered_numbers.append(n)
    if command == 'positive':
        if n >= 0:
            filtered_numbers.append(n)

print(filtered_numbers)

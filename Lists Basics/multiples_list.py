factor = int(input())
count = int(input())

numbers = []

for n in range(1, count + 1):
    numbers.append(n * factor)

print(numbers)

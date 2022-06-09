numbers = list(int(x) for x in input().split())
n = int(input())

for i in range(n):
    numbers.remove(min(numbers))

numbers_str = list(str(x) for x in numbers)

print(', '.join(numbers_str))

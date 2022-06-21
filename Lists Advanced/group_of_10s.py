# Sort the numbers into lists of 10's and print them

from math import ceil

numbers = list(map(int, input().split(", ")))
boundary = ceil(max(numbers) / 10)

current_group = 10

for num in range(1, boundary + 1):
    current_list = [x for x in numbers if x <= current_group]
    numbers = [x for x in numbers if x not in current_list]
    print(f"Group of {current_group}'s: {current_list}")

    current_group += 10

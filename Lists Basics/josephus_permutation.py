numbers = input().split()
special_number = int(input())

index_to_remove = 0

executed = []

while numbers:
    index_to_remove += special_number - 1

    if index_to_remove >= len(numbers):
        index_to_remove %= len(numbers)
    executed.append(numbers.pop(index_to_remove))

print(f"[{','.join(executed)}]")

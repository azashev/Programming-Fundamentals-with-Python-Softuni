numbers = list(map(int, input().split(", ")))
indexes = map(lambda x: x if numbers[x] % 2 == 0 else "None", range(len(numbers)))
final_list = [x for x in indexes if x != "None"]

print(final_list)

# print(list(int(x) for x in input().split() if int(x) % 2 == 0))


numbers = list(map(int, input().split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

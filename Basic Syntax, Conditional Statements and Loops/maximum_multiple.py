divisor = int(input())
boundary = int(input())

max_num = 0

for num in range(1, boundary + 1):
    if num % divisor == 0:
        max_num = num

print(max_num)

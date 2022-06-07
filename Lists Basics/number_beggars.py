numbers = list(int(x) for x in input().split(", "))
count_of_beggars = int(input())
beggars = list(0 for x in range(count_of_beggars))

for i in range(count_of_beggars):
    if i <= len(numbers):
        for value in range(i, len(numbers), count_of_beggars):
            beggars[i] += numbers[value]

print(beggars)

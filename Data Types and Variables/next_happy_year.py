n = int(input())

while True:
    n += 1
    year = ''

    for num in str(n):
        year += num

    if len(set(year)) == len(str(n)):
        print(int(year))
        break

number_of_lines = int(input())

all_are_even = True

for num in range(number_of_lines):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        all_are_even = False
        break
    else:
        continue

if all_are_even:
    print('All numbers are even.')

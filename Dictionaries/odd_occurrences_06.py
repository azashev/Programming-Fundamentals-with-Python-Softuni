# Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it

# •	Words are given on a single line, space-separated
# •	Print the result elements in lowercase, in their order of appearance

symbols = input().split()

my_dict = {}

for symbol in symbols:
    if symbol.lower() in my_dict:
        my_dict[symbol.lower()] += 1
    else:
        my_dict[symbol.lower()] = 1

sort_my_dict = {i: my_dict[i] for i in my_dict if my_dict[i] % 2 != 0}

print(' '.join(sort_my_dict))

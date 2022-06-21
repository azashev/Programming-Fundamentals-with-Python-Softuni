def positives(numbers):
    return [str(x) for x in numbers if x >= 0]


def negatives(numbers):
    return [str(x) for x in numbers if x < 0]


def even(numbers):
    return [str(x) for x in numbers if x % 2 == 0]


def odd(numbers):
    return [str(x) for x in numbers if x % 2 != 0]


input_numbers = list(map(int, input().split(", ")))

print(f"Positive: {', '.join(positives(input_numbers))}")
print(f"Negative: {', '.join(negatives(input_numbers))}")
print(f"Even: {', '.join(even(input_numbers))}")
print(f"Odd: {', '.join(odd(input_numbers))}")

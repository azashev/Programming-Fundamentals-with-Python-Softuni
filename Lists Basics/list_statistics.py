n = int(input())

positives = []
negatives = []

sum_negatives = 0

for num in range(n):
    number = int(input())

    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)
        sum_negatives += number

print(positives)
print(negatives)

print(f"Count of positives: {len(positives)}")
#print(f"Sum of negatives: {sum_negatives}")
print(f"Sum of negatives: {sum(negatives)}")

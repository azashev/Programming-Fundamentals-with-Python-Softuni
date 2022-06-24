# •	Read a sequence of integers and find and print the top 5 numbers greater than the average value in the sequence,
# sorted in descending order
# •	If there are no numbers print "No"
input_numbers = list(map(int, input().split()))

average_number = sum(input_numbers) // len(input_numbers)

input_numbers = [x for x in input_numbers if x > average_number]
top_numbers = []

if not input_numbers:
    print("No")
else:
    for num in range(1, len(input_numbers) + 1):
        top_numbers.append(max(input_numbers))
        input_numbers.remove(max(input_numbers))
        if num == 5:
            break
    print(*top_numbers)

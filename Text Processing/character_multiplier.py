# Create a program that receives two strings on a single line separated by a single space.
# Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0] and add the
# result to the total sum, then continue with the next two characters.
# If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.

first_string, second_string = input().split()

total_sum = 0

if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])

    for i in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[i])

elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(second_string[index]) * ord(first_string[index])

    for i in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[i])

else:
    for index in range(len(first_string)):
        total_sum += ord(second_string[index]) * ord(first_string[index])

print(total_sum)

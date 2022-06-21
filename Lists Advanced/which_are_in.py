first_string = input().split(", ")
second_string = input().split(", ")

# Create a list containing only the strings from the first input line, which are substrings of any string in the second
# input line
result = []

for x in first_string:
    for i in second_string:
        if x in i and x not in result:
            result.append(x)

print(result)

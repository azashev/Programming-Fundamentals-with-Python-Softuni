start_index = int(input())
last_index = int(input())

output = ''

for i in range(start_index, last_index + 1):
    if i == last_index:
        output += chr(i)
    else:
        output += chr(i) + ' '

print(output)

numbers = input().split()
input_string = list(input())

input_string_length = len(input_string)

list_numbers = []

message = ''

for number in numbers:
    current_number = 0
    for x in number:
        current_number += int(x)

    list_numbers.append(current_number)

for index_num in list_numbers:
    counter = index_num

    if counter >= input_string_length:
        looping = True

        while looping:

            for i in range(index_num):

                if i == input_string_length:
                    break

                if counter == 0:
                    message += input_string[i]
                    input_string.pop(i)
                    looping = False
                    break

                counter -= 1

    else:
        message += input_string[counter]
        input_string.pop(index_num)

print(message)

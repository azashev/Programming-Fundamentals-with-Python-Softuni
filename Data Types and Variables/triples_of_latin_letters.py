number = int(input())

for first_char in range(number):
    for second_char in range(number):
        for third_char in range(number):
            print(chr(97 + first_char) + chr(97 + second_char) + chr(97 + third_char))

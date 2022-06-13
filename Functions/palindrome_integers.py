def palindrome(number):
    return number == number[::-1]


input_numbers = input().split(", ")


for number in input_numbers:
    print(palindrome(number))

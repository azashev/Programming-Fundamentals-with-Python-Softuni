key = int(input())
number_of_lines = int(input())

decrypted_message = ''

for i in range(number_of_lines):
    current_letter = input()
    letter_to_ascii = ord(current_letter)
    decrypted_message += chr(letter_to_ascii + key)

print(decrypted_message)

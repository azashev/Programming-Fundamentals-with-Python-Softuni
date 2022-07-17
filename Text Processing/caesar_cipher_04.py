# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing each character with
# the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on.

# Print the encrypted text.

message = input()

encrypted_message = ""

for ch in message:
    encrypted_message += chr(ord(ch) + 3)

print(encrypted_message)

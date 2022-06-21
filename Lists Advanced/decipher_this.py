# Decipher the secret message
# Rules:
# •	the second and the last letter are switched (e.g., Ryade means Ready)
# •	the first letter is replaced by its character code, using ASCII
# Example: 82yade 115te 103o = Ready set go

secret_message = input().split()

deciphered_message = []

for word in secret_message:
    current_word_num = ''

    for ch in word:
        if ch.isdigit():
            current_word_num += ch
            continue
        break
    current_word_char = chr(int(current_word_num))

    word = word.replace(str(current_word_num), '')

    if len(word) > 1:
        new_word = current_word_char + word[-1] + word[1:-1] + word[0]
    else:
        new_word = current_word_char + word
    deciphered_message.append(new_word)

print(*deciphered_message)

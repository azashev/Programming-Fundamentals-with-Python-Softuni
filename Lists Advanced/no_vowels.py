text = input()
vowels = ["a", "o", "u", "e", "i"]

final_text = [x for x in text if x not in vowels]

print(''.join(final_text))

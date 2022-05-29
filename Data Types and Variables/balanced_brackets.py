number_of_lines = int(input())

opening_brackets = 0
closing_brackets = 0

balanced = True

last_bracket = ''

for i in range(number_of_lines):
    command = input()

    if command == last_bracket:
        balanced = False

    last_bracket = command

    if command == "(":
        opening_brackets += 1
    elif command == ")":
        closing_brackets += 1

if not balanced:
    print("UNBALANCED")
elif opening_brackets == closing_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")

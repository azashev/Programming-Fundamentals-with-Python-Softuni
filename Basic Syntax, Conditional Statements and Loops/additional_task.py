import random
from math import floor

initial_jackpot = 100000
bonus_jackpot = 0

numbers_to_guess = int(input("Numbers to guess from a total of 49: "))
cost = 150 * numbers_to_guess

# За всяко число, бонус джакпотът се увеличава с 100
bonus_jackpot += 100 * numbers_to_guess

guess_list = [int(num) for num in input("Enter your numbers, separated by space: ").split()]

correct_guessed_numbers = []
consecutive_correct_guesses = 0
points = 0


for num in guess_list:
    random_number = random.randint(1, 49)
    if num == random_number:
        points += 1
        correct_guessed_numbers.append(num)

# Бонус от последователни познати числа се взима, само при игра с 2 или повече числа
# При познати поне 2 последователни числа, бонусът се добавя към бонус джакпота като сума от
        # броя на сегашните последователни познати числа, умножени по 1000
        if len(guess_list) > 1:
            consecutive_correct_guesses += 1
        if consecutive_correct_guesses > 1:
            bonus_jackpot += consecutive_correct_guesses * 1000

    else:

        # При не познато число, бонус джакпотът се намаля с 100
        bonus_jackpot -= 100

        consecutive_correct_guesses = 0

# Точките се обръщат като процент познати числа
percentage_correct_guessed_numbers = floor((points / numbers_to_guess) * 100)


# Финална печалба: процентът познати числа от първоначалния джакпот + бонус джакпота
prize = ((percentage_correct_guessed_numbers * initial_jackpot) / 100) + bonus_jackpot

if points > 0:
    if points > 1:

        # При 2 или повече познати числа:
        if consecutive_correct_guesses < 2:
            print(f"Поздравления! Ти позна {points} числа и спечели {prize:.2f}лв.")
            print(f"Познатите числа са: {', '.join(str(correct_guessed_numbers))}")
            print(f"Разходи: {cost:.2f}")

        # Ако поне 2 от познатите числа са били последователни:
        else:
            print(f"Поздравления! Ти позна {points} числа, като {consecutive_correct_guesses} от тях "
                  f"позна последователно и спечели {prize:.2f}лв.")
            print(f"Познатите числа са: {', '.join(str(correct_guessed_numbers))}")
            print(f"Разходи: {cost:.2f}")

    # Ако познатото число е само едно:
    else:
        print(f"Поздравления! Ти позна едно число и спечели {prize:.2f}лв.")
        print(f"Познатото число е: {', '.join(str(correct_guessed_numbers))}")
        print(f"Разходи: {cost:.2f}")

# При нито едно познато число:
else:
    print(f"Не позна нито едно число и не печелиш нищо :( опитай пак")
    print(f"Разходи: {cost:.2f}")

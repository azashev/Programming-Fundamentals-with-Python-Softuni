import random

initial_jackpot = 100000
bonus_jackpot = 0

numbers_to_guess = int(input("Numbers to guess from a total of 49: "))

# Бонус от последователни познати числа се взима, само при игра с 2 или повече числа
more_than_one_number_to_guess = False
if numbers_to_guess > 1:
    more_than_one_number_to_guess = True

# За всяко число, бонус джакпотът се увеличава със 100, а разходите със 150
costs = 150 * numbers_to_guess
bonus_jackpot += 100 * numbers_to_guess

guess_list = [int(num) for num in input("Enter your numbers, separated by space: ").split()]
copy_guess_list = guess_list.copy()

correct_guessed_numbers = []
consecutive_correct_guesses = 0
total_consecutive_correct_guesses = 0
points = 0
prize = 0


for num in range(len(guess_list)):
    random_number = random.randint(1, 49)
    if random_number in guess_list:
        points += 1
        guess_list.remove(random_number)
        correct_guessed_numbers.append(str(random_number))

        if more_than_one_number_to_guess:
            consecutive_correct_guesses += 1

        # При познати поне 2 последователни числа, бонусът се добавя към бонус джакпота като сума от
        # броя на сегашните последователни познати числа, умножена по 1000
        if consecutive_correct_guesses > 1:
            bonus_jackpot += consecutive_correct_guesses * 1000

            if consecutive_correct_guesses == 2:
                total_consecutive_correct_guesses += 2
            else:
                total_consecutive_correct_guesses += 1

    else:

        # При не познато число, бонус джакпотът се намаля с 100, а последователните познати числа стават 0
        bonus_jackpot -= 100
        consecutive_correct_guesses = 0

if points > 0:
    # Точките се обръщат като процент познати числа
    percentage_correct_guessed_numbers = round((points / numbers_to_guess) * 100, 2)

    # Финална печалба: процентът познати числа от първоначалния джакпот + бонус джакпота
    prize = ((percentage_correct_guessed_numbers * initial_jackpot) / 100) + bonus_jackpot

# При нито едно познато число:
else:
    print(f"Не позна нито едно число и не печелиш нищо :( опитай пак")
    print(f"Разходи: {costs:.2f}лв.")

final_prize = prize - costs

if points > 0:
    if points > 1:

        # При 2 или повече познати числа:
        if total_consecutive_correct_guesses < 1:
            print(f"Поздравления! Ти позна {points} числа.")
            print(f"Познатите числа са: {', '.join(correct_guessed_numbers)}")
            print(f"Разходи: {costs:.2f}лв.")
            print(f"Крайна печалба: {final_prize:.2f}лв.")

        # Ако поне 2 от познатите числа са били последователни:
        else:
            print(f"Поздравления! Ти позна {points} числа, като {total_consecutive_correct_guesses} от тях "
                  f"позна последователно.")
            print(f"Познатите числа са: {', '.join(correct_guessed_numbers)}")
            print(f"Разходи: {costs:.2f}лв.")
            print(f"Крайна печалба: {final_prize:.2f}лв.")

    # Ако познатото число е само едно:
    else:
        print(f"Поздравления! Ти позна едно число.")
        print(f"Познатото число е: {', '.join(correct_guessed_numbers)}")
        print(f"Разходи: {costs:.2f}лв.")
        print(f"Крайна печалба: {final_prize:.2f}лв.")

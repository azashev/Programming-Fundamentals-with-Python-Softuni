number_of_visited_cities = int(input())

total_profit = 0

for city in range(1, number_of_visited_cities + 1):
    name_current_city = input()
    current_income = float(input())
    current_expenses = float(input())
    if city % 5 == 0:
        current_income -= current_income * 0.1
    elif city % 3 == 0:
        current_expenses += current_expenses / 2

    profit = current_income - current_expenses
    total_profit += profit
    print(f"In {name_current_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")

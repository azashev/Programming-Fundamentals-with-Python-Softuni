companions = int(input())
days_of_the_adventure = int(input())

coins = 0

for day in range(1, days_of_the_adventure + 1):
    coins += 50

    if day % 10 == 0:
        companions -= 2

    if day % 15 == 0:
        companions += 5

    if day % 3 == 0:
        coins -= companions * 3

    if day % 5 == 0:
        coins += companions * 20
        if day % 3 == 0:
            coins -= companions * 2

    coins -= companions * 2

coins_per_companion = int(coins / companions)

print(f"{companions} companions received {coins_per_companion} coins each.")

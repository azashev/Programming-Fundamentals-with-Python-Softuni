events = input().split("|")

energy = 100
coins = 100

events_handled = True

for event in events:
    event = event.split("-")
    current_event = event[0]
    value = int(event[1])

    if current_event == "rest":
        if energy == 100:
            print("You gained 0 energy.")
            print(f"Current energy: {energy}.")
        else:
            if energy + value > 100:
                added_energy = 100 - energy
                energy += added_energy
                print(f"You gained {added_energy} energy.")
                print(f"Current energy: {energy}.")
            else:
                added_energy = value
                energy += added_energy
                print(f"You gained {added_energy} energy.")
                print(f"Current energy: {energy}.")
    elif current_event == "order":
        if energy - 30 >= 0:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print("You had to rest!")
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {current_event}.")
        else:
            events_handled = False
            print(f"Closed! Cannot afford {current_event}.")
            break

if events_handled:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

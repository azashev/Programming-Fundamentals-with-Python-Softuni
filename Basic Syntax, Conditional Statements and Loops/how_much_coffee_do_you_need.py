command = input()

coffees_needed = 0

need_extra_sleep = False

while command != "END":
    if command.lower() == "coding":
        if command.islower():
            coffees_needed += 1
        else:
            coffees_needed += 2

    elif command.lower() == "dog" or command.lower() == "cat":
        if command.islower():
            coffees_needed += 1
        else:
            coffees_needed += 2
    elif command.lower() == "movie":
        if command.islower():
            coffees_needed += 1
        else:
            coffees_needed += 2

    if coffees_needed > 5:
        need_extra_sleep = True
        break

    command = input()

if need_extra_sleep:
    print("You need extra sleep")
else:
    print(coffees_needed)

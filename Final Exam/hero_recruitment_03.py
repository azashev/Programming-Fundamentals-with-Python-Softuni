heroes = {}

while True:
    command_input = input()
    if command_input == "End":
        break

    command = command_input.split()

    if command[0] == "Enroll":
        hero_name = command[1]
        if hero_name not in heroes:
            heroes[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")
    elif command[0] == "Learn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)
    elif command[0] == "Unlearn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name not in heroes[hero_name]:
                print(f"{hero_name} doesn't know {spell_name}.")
            else:
                heroes[hero_name].remove(spell_name)

print("Heroes:")
for key, value in heroes.items():
    print(f"== {key}: {', '.join(value)}")

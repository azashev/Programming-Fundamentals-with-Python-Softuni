name = input()

mentioned_voldemort = False

while name != "Welcome!":
    if name == "Voldemort":
        mentioned_voldemort = True
        print("You must not speak of that name!")
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

    name = input()

if not mentioned_voldemort:
    print("Welcome to Hogwarts.")

gifts = input().split()

command = input().split()

while command != "No Money":
    if len(command) > 0:
        gift = command[1]

        if len(command) == 2:
            index = int(command[2])
            if 0 <= index <= len(gifts):
                gifts[index] = gift

        else:
            if command[0] == "OutOfStock":
                
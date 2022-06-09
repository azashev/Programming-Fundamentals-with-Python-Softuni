gifts = input().split()

command = input()

while command != "No Money":
    split_command = command.split()
    if len(command) > 1:
        gift = split_command[1]

        if len(split_command) == 3:
            index = int(split_command[2])
            if 0 <= index <= len(gifts):
                gifts[index] = gift

        else:
            if split_command[0] == "OutOfStock":
                for element in range(len(gifts)):
                    if gifts[element] == gift:
                        gifts[element] = None
            if split_command[0] == "JustInCase":
                gifts[-1] = gift

    command = input()

for _ in gifts:
    if _ is not None:
        print(_, end=" ")

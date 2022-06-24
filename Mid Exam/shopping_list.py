groceries = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split()
    current_command = command[0]
    current_item = command[1]
    if current_command == "Urgent":
        if current_item not in groceries:
            groceries.insert(0, current_item)
    elif current_command == "Unnecessary":
        if current_item in groceries:
            groceries.remove(current_item)
    elif current_command == "Correct":
        new_item = command[2]
        for x in range(len(groceries)):
            if groceries[x] == current_item:
                groceries[x] = new_item
    elif current_command == "Rearrange":
        if current_item in groceries:
            groceries.remove(current_item)
            groceries.append(current_item)

    command = input()

print(f"{', '.join(groceries)}")

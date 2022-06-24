# Receive an initial list with groceries. After that, you will be receiving 4 types of commands until you receive the
# command "Go Shopping!"
groceries = input().split("!")

command = input()

while command != "Go Shopping!":
    command = command.split()
    current_command = command[0]
    current_item = command[1]

    if current_command == "Urgent":
        # Add the item at the start of the list. If the item already exists, skip this command
        if current_item not in groceries:
            groceries.insert(0, current_item)

    elif current_command == "Unnecessary":
        # Remove the item with the given name, only if it exists in the list. Otherwise, skip this command
        if current_item in groceries:
            groceries.remove(current_item)

    elif current_command == "Correct":
        # If the item with the given old name exists, change its name with the new one. Otherwise, skip this command
        new_item = command[2]
        for x in range(len(groceries)):
            if groceries[x] == current_item:
                groceries[x] = new_item

    elif current_command == "Rearrange":
        # If the grocery exists in the list, remove it from its current position and add it at the end of the list.
        # Otherwise, skip this command
        if current_item in groceries:
            groceries.remove(current_item)
            groceries.append(current_item)

    command = input()

print(f"{', '.join(groceries)}")

list_of_cards = input().split(", ")

n = int(input())

for x in range(n):
    command = input().split(", ")
    action = command[0]

    if action == "Add":
        current_card = command[1]
        if current_card not in list_of_cards:
            list_of_cards.append(current_card)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif action == "Remove":
        current_card = command[1]
        if current_card in list_of_cards:
            list_of_cards.remove(current_card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        current_index = int(command[1])
        if 0 <= current_index < len(list_of_cards):
            list_of_cards.pop(current_index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif action == "Insert":
        current_index = int(command[1])
        current_card = command[2]

        if 0 <= current_index < len(list_of_cards):
            if current_card not in list_of_cards:
                list_of_cards.insert(current_index, current_card)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(', '.join(list_of_cards))

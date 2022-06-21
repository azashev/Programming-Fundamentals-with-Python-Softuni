# the number of rooms in the business center
number_of_rooms = int(input())

free_chairs = 0
game_on = True

for room in range(1, number_of_rooms + 1):

    # information about the chairs in the room and the number of visitors
    # Example: "XXXXX 4" (5 chairs and 4 visitors)
    current_room = input().split()

    available_chairs = len(current_room[0])
    visitors = int(current_room[1])

    if visitors > available_chairs:
        game_on = False
        needed_chairs = visitors - available_chairs

        # If there are not enough chairs in a specific room, print a message:
        print(f"{needed_chairs} more chairs needed in room {room}")
    else:
        free_chairs += available_chairs - visitors

# If there are enough chairs in all rooms, print the following message:
if game_on:
    print(f"Game On, {free_chairs} free chairs left")

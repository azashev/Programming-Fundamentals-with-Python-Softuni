number_of_pieces = int(input())

pieces = {}

for x in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces[piece] = [composer, key]

while True:
    command = input()
    if command == "Stop":
        break

    command = command.split("|")

    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]

        if piece not in pieces:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]

        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]

        if piece in pieces:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in pieces.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")


# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in this format:
# "{piece}|{composer}|{key}"
#
# You will then receive different commands, each on a new line, separated by "|" until the "Stop" command is given:
# • "Add|{piece}|{composer}|{key}":
#   - You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
#
#   - If the piece is already in the collection, print:
# "{piece} is already in the collection!"
#
# • "Remove|{piece}":
#   - If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
#
#   - Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
#
# • "ChangeKey|{piece}|{new key}":
#   - If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
#
#   - Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
#
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
#
# Input/Constraints:
# • You will receive a single integer at first – the initial number of pieces in the collection
# • For each piece, you will receive a single line of text with information about it.
# • Then you will receive multiple commands in the way described above until the command "Stop".
#
# Output:
# • All the output messages with the appropriate formats are described in the problem description.

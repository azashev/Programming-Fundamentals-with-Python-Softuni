n = int(input())

plants = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)

    plants[plant] = {"rarity": rarity, "ratings": []}

while True:
    command_input = input()
    if command_input == "Exhibition":
        break

    current_command = command_input.split(": ")

    if current_command[0] == "Rate":
        plant, rating = current_command[1].split(" - ")
        if plant in plants:
            rating = int(rating)
            plants[plant]["ratings"].append(rating)
        else:
            print("error")
            continue

    elif current_command[0] == "Update":
        plant, rarity = current_command[1].split(" - ")
        if plant in plants:
            rarity = int(rarity)

            plants[plant]["rarity"] = rarity
        else:
            print("error")
            continue

    elif current_command[0] == "Reset":
        plant = current_command[1]

        if plant in plants:
            plants[plant]["ratings"] = []
        else:
            print("error")
            continue

print("Plants for the exhibition:")
for key, value in plants.items():
    if plants[key]['ratings']:
        plants[key]['average_rating'] = sum(value['ratings']) / len(value['ratings'])
    else:
        plants[key]["average_rating"] = 0
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['average_rating']:.2f}")


# On the first line, you will receive a number n. On the next n lines, you will be given some information about the
# plants that you have discovered in the format: "{plant}<->{rarity}".
# Store that information because it will be needed later. If you receive a plant more than once, update its rarity.
#
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# • "Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# • "Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# • "Reset: {plant}" – remove all the ratings of the given plant
#
# Note: If any given plant name is invalid, print "error"
#
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
#
# The average rating should be formatted to the second decimal place.
#
#
# Input / Constraints:
# • You will receive the input as described above
# • JavaScript: you will receive a list of strings
#
# Output:
# • Print the information about all plants as described above

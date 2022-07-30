cities = {}

while True:
    targeted_city = input().split("||")
    if targeted_city[0] == "Sail":
        break

    city = targeted_city[0]
    population = int(targeted_city[1])
    gold = int(targeted_city[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

while True:
    event = input().split("=>")
    if event[0] == "End":
        break

    current_event = event[0]
    if current_event == "Plunder":
        town = event[1]
        people = int(event[2])
        current_gold = int(event[3])

        cities[town]["population"] -= people
        cities[town]["gold"] -= current_gold

        print(f"{town} plundered! {current_gold} gold stolen, {people} citizens killed.")

        if cities[town]["population"] < 1 or cities[town]["gold"] < 1:
            del cities[town]
            print(f"{town} has been wiped off the map!")

    elif current_event == "Prosper":
        town = event[1]
        current_gold = int(event[2])

        if current_gold < 0:
            print("Gold added cannot be a negative number!")
            continue

        cities[town]["gold"] += current_gold
        print(f"{current_gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, values in cities.items():
        print(f"{city} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


# Until the "Sail" command is given, you will be receiving:
# • You and your crew have targeted cities, with their population and gold, separated by "||".
# • If you receive a city that has already been received, increase the population and gold with the given values.
#
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# • "Plunder=>{town}=>{people}=>{gold}"
#   - You have successfully attacked and plundered the town, killing the given number of people and stealing the
#   respective amount of gold.
#   - For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
#   - If any of those two values (population or gold) reaches zero, the town is disbanded.
#        You need to remove it from your collection of targeted cities and print the following message: "{town} has
#       been wiped off the map!"
#   - There will be no case of receiving more people or gold than there is in the city.
#
# • "Prosper=>{town}=>{gold}"
#   - There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
#   - The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print:
#   "Gold added cannot be a negative number!" and ignore the command.
#   - If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the
#   following message:
# "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
#
#
# Input:
# • On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold
# and population, separated by "||"
# • On the following lines, until the "End" command, you will be receiving strings representing the actions described
# above, separated by "=>"
#
# Output:
# • After receiving the "End" command, if there are any existing settlements on your list of targets, you need to print
# all of them, in the following format:
# "Ahoy, Captain! There are {count} wealthy settlements to go to:
# {town1} -> Population: {people} citizens, Gold: {gold} kg
# {town2} -> Population: {people} citizens, Gold: {gold} kg
#  ...
# {town...n} -> Population: {people} citizens, Gold: {gold} kg"
#
# • If there are no settlements left to plunder, print:
# "Ahoy, Captain! All targets have been plundered and destroyed!"
#
#
# Constraints:
# • The initial population and gold of the settlements will be valid 32-bit integers, never negative, or exceed the
# respective limits.
# • The town names in the events will always be valid towns that should be on your list.

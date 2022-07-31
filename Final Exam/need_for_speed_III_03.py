n = int(input())

cars = {}

for car_ in range(n):
    car = input().split("|")
    current_car = car[0]
    mileage = int(car[1])
    fuel = int(car[2])

    cars[current_car] = {"mileage": mileage, "fuel": fuel}

while True:
    command = input()

    if command == "Stop":
        break

    command = command.split(" : ")
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])

        if fuel > cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if cars[car]["fuel"] + fuel > 75:
            fuel = 75 - cars[car]["fuel"]
            cars[car]["fuel"] = 75
        else:
            cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])

        if cars[car]["mileage"] - kilometers < 10000:
            cars[car]["mileage"] = 10000
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in cars.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")


# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain.
# On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the
# following format:
# "{car}|{mileage}|{fuel}"
#
#
# Then, you will be receiving different commands, each on a new line, separated by " : ", until you receive the
# "Stop" command:
#
# • "Drive : {car} : {distance} : {fuel}":
#   - You need to drive the given distance, and you will need the given fuel to do that.
#   If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
#   - If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its
#   fuel with the given fuel, and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
#   - You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and
#   print: "Time to sell the {car}!"
#
# •	"Refuel : {car} : {fuel}":
#   - Refill the tank of your car.
#   - Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the
#   tank, take only what is required to fill it up.
#   - Print a message in the following format: "{car} refueled with {fuel} liters"
#
# • "Revert : {car} : {kilometers}":
#   - Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it
#   with in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
#   - If the mileage becomes less than 10 000km after decreasing it, just set it to 10 000km and do NOT print anything.
#
#
# Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
#
#
# Input/Constraints:
# • The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
# • The fuel and distance amounts in the commands will never be negative.
# • The car names in the commands will always be valid cars in your possession.
#
# Output:
# • All the output messages with the appropriate formats are described in the problem description.

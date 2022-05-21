animals = input().split(", ")

position_counter = 1

for i in range(len(animals) - 1, - 1, - 1):
    if animals[i] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if animals[i - 1] == "wolf":
        print(f"Oi! Sheep number {position_counter}! You are about to be eaten by a wolf!")
        break
    position_counter += 1

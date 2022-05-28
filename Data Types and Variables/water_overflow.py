number_of_lines = int(input())

capacity = 255

for i in range(number_of_lines):
    liters_of_water_to_pour = int(input())

    if capacity - liters_of_water_to_pour < 0:
        print("Insufficient capacity!")
        continue

    capacity -= liters_of_water_to_pour

print(255 - capacity)

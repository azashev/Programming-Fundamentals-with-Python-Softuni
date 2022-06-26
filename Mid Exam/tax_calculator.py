from math import floor

vehicles = input().split(">>")

total_taxes = 0

for vehicle in vehicles:
    current_vehicle = vehicle.split()
    current_car_type = current_vehicle[0]
    years = int(current_vehicle[1])
    kilometers_travelled = int(current_vehicle[2])
    if current_car_type == "family":
        initial_tax = 50
        tax_declines = 5 * years
        tax_increase = 12 * floor(kilometers_travelled / 3000)
        tax_to_pay = initial_tax + tax_increase - tax_declines
        total_taxes += tax_to_pay
    elif current_car_type == "heavyDuty":
        initial_tax = 80
        tax_declines = 8 * years
        tax_increase = 14 * floor(kilometers_travelled / 9000)
        tax_to_pay = initial_tax + tax_increase - tax_declines
        total_taxes += tax_to_pay
    elif current_car_type == "sports":
        initial_tax = 100
        tax_declines = 9 * years
        tax_increase = 18 * floor(kilometers_travelled / 2000)
        tax_to_pay = initial_tax + tax_increase - tax_declines
        total_taxes += tax_to_pay
    else:
        print("Invalid car type.")
        continue

    print(f"A {current_car_type} car will pay {tax_to_pay:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")

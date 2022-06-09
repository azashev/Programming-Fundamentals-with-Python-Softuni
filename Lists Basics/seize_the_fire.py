fires_and_cells = input().split("#")
water = int(input())

effort = 0
total_fire = 0
distinguished_cells = []

for x in fires_and_cells:
    current_fire = x.split(" = ")
    current_fire_type, current_cell_value = current_fire[0], int(current_fire[1])

    if current_fire_type == "High":
        if 81 <= current_cell_value <= 125 and water >= current_cell_value:
            water -= current_cell_value
            effort += current_cell_value * 0.25
            total_fire += current_cell_value
            distinguished_cells.append(current_cell_value)
    if current_fire_type == "Medium":
        if 51 <= current_cell_value <= 80 and water >= current_cell_value:
            water -= current_cell_value
            effort += current_cell_value * 0.25
            total_fire += current_cell_value
            distinguished_cells.append(current_cell_value)
    if current_fire_type == "Low":
        if 1 <= current_cell_value <= 50 and water >= current_cell_value:
            water -= current_cell_value
            effort += current_cell_value * 0.25
            total_fire += current_cell_value
            distinguished_cells.append(current_cell_value)

print("Cells:")

for element in distinguished_cells:
    print(f"- {element}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

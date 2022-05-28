lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_repairs = (lost_fights // 2) * helmet_price
sword_repairs = (lost_fights // 3) * sword_price
shield_repairs = (lost_fights // 6) * shield_price
armor_repairs = ((lost_fights // 6) // 2) * armor_price

expenses = helmet_repairs + sword_repairs + shield_repairs + armor_repairs

print(f"Gladiator expenses: {expenses:.2f} aureus")

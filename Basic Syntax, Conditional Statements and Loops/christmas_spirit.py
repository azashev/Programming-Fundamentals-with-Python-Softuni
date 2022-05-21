quantity_of_decorations_to_buy = int(input())
days_left_until_christmas = int(input())

ornament_set, ornament_set_spirit = 2, 5
tree_skirt, tree_skirt_spirit = 5, 3
tree_garland, tree_garland_spirit = 3, 10
tree_lights, tree_lights_spirit = 15, 17

budget = 0
spirit = 0

for day in range(1, days_left_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations_to_buy += 2

    if day % 2 == 0:
        budget += ornament_set * quantity_of_decorations_to_buy
        spirit += ornament_set_spirit
    if day % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity_of_decorations_to_buy
        spirit += tree_skirt_spirit + tree_garland_spirit
    if day % 5 == 0:
        budget += tree_lights * quantity_of_decorations_to_buy
        spirit += tree_lights_spirit
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += tree_skirt + tree_garland + tree_lights

if days_left_until_christmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")

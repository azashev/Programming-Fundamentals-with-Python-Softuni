# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes

# "Shards", "Fragments", and "Motes" are the key materials (case-insensitive), and everything else is junk.

# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# The first key material that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.

# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"

# Finally, print the collected junk items in the order of appearance.

def material_checker(_material):
    if _material == "shards":
        return f"Shadowmourne obtained!"
    elif _material == "fragments":
        return f"Valanyr obtained!"
    else:
        return f"Dragonwrath obtained!"


valuable_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

collected_material = ''

items = input().split()

while True:
    for item in range(0, len(items), 2):
        quantity = int(items[item])
        material = items[item + 1].lower()

        if material in valuable_materials:
            valuable_materials[material] += quantity
            if valuable_materials[material] >= 250:
                collected_material = material
                valuable_materials[material] -= 250

                print(material_checker(collected_material))
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity
    if collected_material:
        break
    items = input().split()

for material, quantity in valuable_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk.items():
    print(f"{material}: {quantity}")

budget = float(input())

price_per_kg_flour = float(input())
price_for_pack_of_eggs = price_per_kg_flour * 0.75
price_for_liter_milk = price_per_kg_flour * 1.25

recipe = price_per_kg_flour + price_for_pack_of_eggs + (price_for_liter_milk * 0.25)

breads_count = 0
colored_eggs = 0

while budget > 0:
    if budget - recipe > 0:
        budget -= recipe
        breads_count += 1
        colored_eggs += 3

        if breads_count % 3 == 0:
            colored_eggs -= breads_count - 2
    else:
        break
print(f"You made {breads_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

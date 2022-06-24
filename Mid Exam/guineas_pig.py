# Merry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store and
# buys him everything he needs – food, hay, and cover.

# Every day Puppy eats 300 gr of food
# Every second day Merry gives it a certain amount of hay equal to 5% of the rest of the food
# Every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight

# Calculate whether the quantity of food, hay, and cover, will be enough for a month (30 days)

def food_checker(food, hay, cover):
    return food > 0 and hay > 0 and cover > 0


# the quantities are received in kilograms, so we turn them into grams
quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
guineas_weight = float(input()) * 1000

for day in range(1, 31):
    quantity_food -= 300

    if day % 2 == 0:
        quantity_hay -= (quantity_food * 5) / 100
    if day % 3 == 0:
        quantity_cover -= guineas_weight // 3

# if the food, the hay, and teh cover are enough for a month:
if food_checker(quantity_food, quantity_hay, quantity_cover):
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {quantity_hay / 1000:.2f}, "
          f"Cover: {quantity_cover / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")

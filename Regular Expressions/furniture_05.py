# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format:
# ">>{furniture_name}<<{price}!{quantity}".
#
# The price could be a floating-point or integer number.
# You should store the names of the furniture and the total price.
#
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"

import re

command = input()

pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)\b"

bought_furniture = []
total_price = 0


# Solution one:

while not command == "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        price = float(price)
        quantity = int(quantity)
        total_price += price * quantity
    command = input()

print("Bought furniture:")
for x in bought_furniture:
    print(x)
print(f"Total money spend: {total_price:.2f}")


# Solution two:

# while not command == "Purchase":
#     match = re.findall(pattern, command)
#     if match:
#         furniture.append(match[0][0])
#         price = float(match[0][1])
#         quantity = int(match[0][2])
#         total_price += price * quantity
#     command = input()
#
# print("Bought furniture:")
# for x in furniture:
#     print(x)
# print(f"Total money spend: {total_price:.2f}")

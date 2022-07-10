# Write a program that keeps the information about products and their prices. Each product has a name, price, and quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is
# different, replace the price as well.

# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy",keep adding
# items. Finally, print all items with their names and the total price of each product.

# Input:
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.

# Output:
# •	Print information about each product in the following format:
# "{product_name} -> {total_price}"
# •	Format the total price to the 2nd digit after the decimal separator.

products = {}

command = input()

while not command == "buy":
    command = command.split()
    product_name = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product_name not in products:
        products[product_name] = [price, quantity]
    else:
        products[product_name][0] = price
        products[product_name][1] += quantity

    command = input()

for product, value in products.items():
    print(f"{product} -> {(value[0] * value[1]):.2f}")

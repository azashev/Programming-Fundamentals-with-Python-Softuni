# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once. In that case, add the new quantity to the existing product.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"

products_list = input()

products = {}

while not products_list == "statistics":
    current_product, quantity = products_list.split(": ")
    quantity = int(quantity)

    if current_product in products:
        products[current_product] += quantity
    else:
        products[current_product] = quantity

    products_list = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")

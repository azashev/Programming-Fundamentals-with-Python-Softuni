products_input = input().split()
products_to_search = input().split()

products = {}

for x in range(0, len(products_input), 2):
    current_product = products_input[x]
    value = int(products_input[x + 1])

    products[current_product] = value


for product in products_to_search:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

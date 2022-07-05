# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".

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

def order(product, quantity):
    if product == "coffee":
        return f"{quantity * 1.50:.2f}"
    elif product == "water":
        return f"{quantity * 1:.2f}"
    elif product == "coke":
        return f"{quantity * 1.40:.2f}"
    elif product == "snacks":
        return f"{quantity * 2:.2f}"


input_product = input()
input_quantity = int(input())

print(order(input_product, input_quantity))

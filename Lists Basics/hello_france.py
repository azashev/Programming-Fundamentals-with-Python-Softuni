items = input().split("|")
budget = float(input())

ticket_price = 150

items_new_prices = []
profit = 0

for item in items:
    item = item.split("->")
    item_type = item[0]
    item_price = float(item[1])

    if item_type == "Clothes" and item_price <= 50:
        if budget >= item_price:
            budget -= item_price
            items_new_prices.append(item_price + (item_price * 0.4))
            profit += ((item_price + (item_price * 0.4)) - item_price)
    elif item_type == "Shoes" and item_price <= 35:
        if budget >= item_price:
            budget -= item_price
            items_new_prices.append(item_price + (item_price * 0.4))
            profit += ((item_price + (item_price * 0.4)) - item_price)
    elif item_type == "Accessories" and item_price <= 20.50:
        if budget >= item_price:
            budget -= item_price
            items_new_prices.append(item_price + (item_price * 0.4))
            profit += ((item_price + (item_price * 0.4)) - item_price)

for i in items_new_prices:
    budget += i
    print(f'{i:.2f}', end=' ')
print()
print(f"Profit: {profit:.2f}")

if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")

number_of_orders = int(input())

total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        price_for_the_day = (capsules_needed_per_day * price_per_capsule) * days
        total_price += price_for_the_day
        print(f"The price for the coffee is: ${price_for_the_day:.2f}")
    else:
        continue

print(f"Total: ${total_price:.2f}")

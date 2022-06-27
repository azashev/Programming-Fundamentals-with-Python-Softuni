# Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax)
# until you receive what type of customer this is - special or regular. Once you receive the type of customer, print the receipt

# The taxes are 20% of each part's price you receive
# If the customer is special, he has a 10% discount on the total price with taxes
# If a given price is not a positive number, then print "Invalid price!" and continue with the next price
# If the total price is equal to zero, print "Invalid order!"

price = input()

total_price_no_tax = 0
total_price_with_tax = 0
total_tax = 0

while True:
    if price == "special":
        total_price_with_tax -= total_price_with_tax * 0.1
        break
    elif price == "regular":
        break

    else:
        price = float(price)
        if price < 1:
            print("Invalid price!")
        else:
            total_price_no_tax += price
            total_tax += price * 0.2
            total_price_with_tax += price + (price * 0.2)

    price = input()

if not total_price_with_tax == 0:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price_no_tax:.2f}$\n"
          f"Taxes: {total_tax:.2f}$\n-----------\nTotal price: {total_price_with_tax:.2f}$")
else:
    print("Invalid order!")

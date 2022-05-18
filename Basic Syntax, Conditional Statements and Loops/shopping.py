budget = float(input())

overdraft = False

command = input()

while command != 'End':
    new_product_price = float(command)
    budget -= new_product_price

    if budget < 0:
        print('You went in overdraft!')
        overdraft = True
        break

    command = input()

if not overdraft:
    print('You bought everything needed.')

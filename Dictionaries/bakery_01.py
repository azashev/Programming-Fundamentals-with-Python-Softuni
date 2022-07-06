# You will receive a single line containing some food (keys) and quantities (values). They will be separated by a single
# space (the first element is the key, the second – the value, and so on).

# Create a dictionary with all the keys and values and print it on the console

elements = input().split()

bakery = {}

# for loop solution
# for x in range(0, len(elements), 2):
    # food = elements[x]
    # quantity = int(elements[x + 1])
    #
    # bakery[food] = quantity

    #
    # bakery[elements[x]] = int(elements[x])

# comprehension
bakery_dict = {elements[i]: int(elements[i + 1]) for i in range(0, len(elements), 2)}

print(bakery)

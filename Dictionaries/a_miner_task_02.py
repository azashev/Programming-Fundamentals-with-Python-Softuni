# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.

# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"

resource = input()

collected_resources = {}

while not resource == "stop":
    quantity = int(input())

    if resource not in collected_resources:
        collected_resources[resource] = quantity
    else:
        collected_resources[resource] += quantity

    resource = input()

for resource, quantity in collected_resources.items():
    print(f"{resource} -> {quantity}")

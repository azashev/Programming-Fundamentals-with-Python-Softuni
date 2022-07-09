# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.

# After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact
# by name and print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."

entry = input()

phonebook = {}

while "-" in entry:
    name, phone_number = entry.split("-")
    phonebook[name] = phone_number

    entry = input()

names_to_check = int(entry)

for x in range(names_to_check):
    name_to_check = input()
    if name_to_check in phonebook:
        print(f"{name_to_check} -> {phonebook[name_to_check]}")
    else:
        print(f"Contact {name_to_check} does not exist.")

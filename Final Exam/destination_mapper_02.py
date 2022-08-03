import re

places = input()

pattern = r"(=([A-Z][A-Za-z]{2,})=|\/([A-Z][A-Za-z]{2,})\/)"

matches = re.finditer(pattern, places)

valid_locations = []
points = 0

for match in matches:
    if "=" in match.group():
        match = match.group().strip("=")
    elif "/" in match.group():
        match = match.group().strip("/")
    points += len(match)
    valid_locations.append(match)

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {points}")


# On the first line, you will be given a string containing all of your stops.
# Until you receive the command "Travel", you will be given some commands to manipulate that initial string.
#
# The commands can be:
# • "Add Stop:{index}:{string}":
#   - Insert the given string at that index only if the index is valid
# • "Remove Stop:{start_index}:{end_index}":
#   - Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# • "Switch:{old_string}:{new_string}":
#   - If the old string is in the initial string, replace it with the new one (all occurrences)
#
# Note: After each command, print the current state of the string if it is valid!
#
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
#
# Input / Constraints:
# • JavaScript: you will receive a list of strings
# • An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
#
# Output:
# Print the proper output messages in the proper cases as described in the problem description

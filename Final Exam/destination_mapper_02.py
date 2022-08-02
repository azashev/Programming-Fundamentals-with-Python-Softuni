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

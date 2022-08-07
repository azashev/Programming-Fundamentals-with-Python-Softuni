import re

text_string = input()

pattern = r"((@|#)+([a-z]{3,})(@|#+)([^A-Za-z0-9]+)?/{1,}(\d+)(/{1,}))"

matches = re.finditer(pattern, text_string)
for m in matches:
    print(f"You found {m.group(6)} {m.group(3)} eggs!")

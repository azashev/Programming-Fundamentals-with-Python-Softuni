a = int(input())
b = int(input())

c = a

print(f"Before:\n"
      f"a = {a}\n"
      f"b = {b}")

a = b
b = c

print(f"After:\n"
      f"a = {a}\n"
      f"b = {b}")

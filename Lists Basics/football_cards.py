a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]

terminated = False
cards = input().split()

for card in cards:
    if card in a:
        a.remove(card)
    elif card in b:
        b.remove(card)

    if len(a) < 7 or len(b) < 7:
        terminated = True
        break

print(f"Team A - {len(a)}; Team B - {len(b)}")

if terminated:
    print("Game was terminated")

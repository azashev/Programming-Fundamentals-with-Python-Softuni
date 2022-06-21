text = [x for x in input().split() if len(x) % 2 == 0]
print(*text, sep='\n')

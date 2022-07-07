# Write a program that receives a list of characters separated by ", ". It should create a dictionary with each character
# as a key and its ASCII value as a value, using comprehension.

dict_comprehension = {x: ord(x) for x in input().split(", ")}

print(dict_comprehension)

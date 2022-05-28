from math import ceil

people = int(input())
capacity = int(input())

courses = ceil(people / capacity)
print(courses)

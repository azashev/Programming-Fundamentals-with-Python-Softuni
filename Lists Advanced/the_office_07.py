employees_happiness = [int(x) for x in input().split()]
factor = int(input())

employees_happiness = [x * factor for x in employees_happiness]

average = sum(employees_happiness) / len(employees_happiness)

counter = 0

for i in employees_happiness:
    if i >= average:
        counter += 1

if counter >= len(employees_happiness) / 2:
    print(f"Score: {counter}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(employees_happiness)}. Employees are not happy!")


# You will receive two lines of input:
# • a list of employees' happiness as a string of numbers separated by a single space
# • a happiness improvement factor (single number).
#
# Your task is to find out if the employees are generally happy in their office.
#
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
#
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

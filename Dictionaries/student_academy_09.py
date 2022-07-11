# Write a program that keeps the information about students and their grades.

# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will
# be receiving each student's name and their grade.

# Keep track of all grades for each student and keep only students with an average grade higher than or equal to 4.50

# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

def average_grade_checker(grades):
    calculate_average_grade = sum(grades) / len(grades)
    if calculate_average_grade >= 4.50:
        return f"{calculate_average_grade:.2f}"
    return False


n = int(input())

students = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in students:
        students[student] = []
    students[student].append(grade)

qualified_students = {f: average_grade_checker(students[f]) for f in students if average_grade_checker(students[f])}

print(*[f"{student} -> {grade}" for student, grade in qualified_students.items()], sep="\n")

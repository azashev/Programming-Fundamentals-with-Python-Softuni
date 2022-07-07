# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}"
# On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines.

# Note: each student's ID will always be unique

command = input()

my_dict = {}

while True:
    if ":" in command:
        student_name, student_id, student_course = command.split(":")
    else:
        break

    student_id = int(student_id)

    my_dict[student_name] = []
    my_dict[student_name].append(student_id)
    my_dict[student_name].append(student_course)

    command = input()

command = command.replace("_", " ")

for student, value in my_dict.items():
    if command == value[1]:
        print(f"{student} - {value[0]}")

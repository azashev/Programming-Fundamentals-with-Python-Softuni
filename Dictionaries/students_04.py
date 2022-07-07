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

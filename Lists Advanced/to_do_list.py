notes = [0] * 10
command = input()

while command != "End":
    command = command.split("-")
    current_priority = int(command[0]) - 1
    current_note = command[1]

    notes.pop(current_priority)
    notes.insert(current_priority, current_note)

    command = input()

to_do_list = [x for x in notes if x != 0]

print(to_do_list)

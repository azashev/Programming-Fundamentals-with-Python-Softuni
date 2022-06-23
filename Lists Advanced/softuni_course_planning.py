def lesson_checker(title, lessons):
    return title in lessons


initial_schedule_of_lessons = input().split(", ")

command = input()

while command != "course start":
    current_command = command.split(":")
    action = current_command[0]
    lesson_title = current_command[1]

    if action == "Add":
        # add the lesson to the end of the schedule if it does not exist
        if lesson_title not in initial_schedule_of_lessons:
            initial_schedule_of_lessons.append(lesson_title)
    elif action == "Insert":
        # insert the lesson to the given index, if it does not exist
        current_index = int(current_command[2])
        if lesson_title not in initial_schedule_of_lessons:
            initial_schedule_of_lessons.insert(current_index, lesson_title)
    elif action == "Remove":
        # remove the lesson, if it exists
        if lesson_title in initial_schedule_of_lessons:
            initial_schedule_of_lessons.remove(lesson_title)

        if f"{lesson_title}-Exercise" in initial_schedule_of_lessons:
            initial_schedule_of_lessons.remove(f"{lesson_title}-Exercise")
    elif action == "Swap":
        # swap the position of the two lessons if they exist

        second_lesson_title = current_command[2]
        if lesson_title in initial_schedule_of_lessons and second_lesson_title in initial_schedule_of_lessons:
            index_lesson_title = initial_schedule_of_lessons.index(lesson_title)
            index_second_lesson_title = initial_schedule_of_lessons.index(second_lesson_title)
            initial_schedule_of_lessons[index_lesson_title], initial_schedule_of_lessons[index_second_lesson_title] = \
                initial_schedule_of_lessons[index_second_lesson_title], initial_schedule_of_lessons[index_lesson_title]
        if f"{lesson_title}-Exercise" in initial_schedule_of_lessons and f"{second_lesson_title}-Exercise" in \
                initial_schedule_of_lessons:
            index_lesson_exercise = initial_schedule_of_lessons.index(f"{lesson_title}-Exercise")
            index_second_lesson_exercise = initial_schedule_of_lessons.index(f"{second_lesson_title}-Exercise")
            initial_schedule_of_lessons[index_lesson_exercise], \
            initial_schedule_of_lessons[index_second_lesson_exercise] = \
                initial_schedule_of_lessons[index_second_lesson_exercise], \
                initial_schedule_of_lessons[index_lesson_exercise]
        elif f"{lesson_title}-Exercise" in initial_schedule_of_lessons:
            index_lesson_title = initial_schedule_of_lessons.index(lesson_title)
            initial_schedule_of_lessons.remove(f"{lesson_title}-Exercise")
            initial_schedule_of_lessons.insert(index_lesson_title, f"{lesson_title}-Exercise")
        elif f"{second_lesson_title}-Exercise" in initial_schedule_of_lessons:
            index_second_lesson_title = initial_schedule_of_lessons.index(second_lesson_title)
            initial_schedule_of_lessons.remove(f"{second_lesson_title}-Exercise")
            initial_schedule_of_lessons.insert(index_second_lesson_title + 1, f"{second_lesson_title}-Exercise")

    elif action == "Exercise":
        # add Exercise in the schedule right after the lesson index, if the lesson exists and there is no exercise
        # already, in the following format "{lessonTitle}-Exercise". If the lesson doesn't exist, add the lesson
        # at the end of the course schedule, followed by the Exercise
        #
        # Each time you Swap or Remove a lesson, you should do the same with the Exercises, if there are any following
        # the lessons
        if lesson_title in initial_schedule_of_lessons and f"{lesson_title}-Exercise" not in initial_schedule_of_lessons:
            index_lesson_title = initial_schedule_of_lessons.index(lesson_title)
            initial_schedule_of_lessons.insert(index_lesson_title + 1, f"{lesson_title}-Exercise")
        elif lesson_title not in initial_schedule_of_lessons:
            initial_schedule_of_lessons.append(lesson_title)
            initial_schedule_of_lessons.append(f"{lesson_title}-Exercise")

    command = input()

for lesson in range(len(initial_schedule_of_lessons)):
    print(f"{lesson + 1}.{initial_schedule_of_lessons[lesson]}")


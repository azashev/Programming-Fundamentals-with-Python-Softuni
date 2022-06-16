numbers = list(map(int, input().split()))

total_time_first_car = 0
total_time_second_car = 0

times_first_car = []
times_second_car = []

middle_index = len(numbers) // 2

# calculations for the first car
for index in range(0, middle_index):
    if numbers[index] == 0:
        total_time_first_car -= total_time_first_car * 0.2
    else:
        total_time_first_car += numbers[index]


# calculations for the second car
for index in range(middle_index + 1, len(numbers)):
    if numbers[index] == 0:
        total_time_second_car -= total_time_second_car * 0.2
    else:
        total_time_second_car += numbers[index]

if total_time_first_car < total_time_second_car:
    print(f"The winner is left with total time: {total_time_first_car:.1f}")
elif total_time_second_car < total_time_first_car:
    print(f"The winner is right with total time: {total_time_second_car:.1f}")

# Problem: Write a program that finds a place for the tourist on a lift
#
# Every wagon (element in the list) should have a maximum of 4 people on it. If a wagon is full, direct the people
# to the next one that has available space

waiting_people = int(input())
lift = list(map(int, input().split()))

for i in range(len(lift)):
    if lift[i] < 4:
        if waiting_people - (4 - lift[i]) >= 0:
            waiting_people -= 4 - lift[i]
            lift[i] += 4 - lift[i]
        else:
            lift[i] += waiting_people
            waiting_people = 0
            break

# When there is no more available space left on the lift, or there are no more people in the queue, then print the
# final state of the lift's wagons and one of the following messages:

if waiting_people > 0:
    # If there are still people in the queue and but there is no available space:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(*lift, sep=' ')
else:
    # If the lift is full and there are no more people in the queue, print only the wagons:
    if sum(lift) == len(lift) * 4:
        print(*lift, sep=' ')
    else:
        # If there are no more people in the queue and the lift has empty spots:
        print("The lift has empty spots!")
        print(*lift, sep=' ')

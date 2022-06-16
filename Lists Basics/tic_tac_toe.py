first_line = list(map(int, input().split()))
second_line = list(map(int, input().split()))
third_line = list(map(int, input().split()))

first_player_wins = False
second_player_wins = False


# checking for connections on a single line

if len(set(first_line)) == 1:
    if first_line[0] == 1:
        print("First player won")
        exit()
    elif first_line[0] == 2:
        print("Second player won")
        exit()
elif len(set(second_line)) == 1:
    if second_line[0] == 1:
        print("First player won")
        exit()
    elif second_line[0] == 2:
        print("Second player won")
        exit()
elif len(set(third_line)) == 1:
    if third_line[0] == 1:
        print("First player won")
        exit()
    elif third_line[0] == 2:
        print("Second player won")
        exit()


# starting iterations for every line to check for connections

for index_first_line in range(3):
    for index_second_line in range(3):
        for index_third_line in range(3):
            if index_first_line == index_second_line == index_third_line or\
                    index_first_line == (index_second_line + 1) == (index_third_line + 2) or\
                    index_first_line == (index_second_line - 1) == (index_third_line - 2):

                if first_line[index_first_line] == second_line[index_second_line] == third_line[index_third_line]:
                    if first_line[index_first_line] == 1:
                        first_player_wins = True
                        break
                    elif first_line[index_first_line] == 2:
                        second_player_wins = True
                        break

if first_player_wins:
    print("First player won")
elif second_player_wins:
    print("Second player won")
else:
    print("Draw!")

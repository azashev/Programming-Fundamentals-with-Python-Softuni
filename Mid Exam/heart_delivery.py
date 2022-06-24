# Receive a string with even integers, separated by a "@" - this is our neighborhood. After that, a series of commands
# will follow until you receive the command "Love!".
# Every house in the neighborhood needs a certain number of hearts delivered by Cupid so it can celebrate Valentine's
# day. The integers in the neighborhood indicate those needed hearts.
# Cupid starts at the position of the first house and must jump by a given length

# Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2

# • If the needed hearts for a certain house become equal to 0, print on the console "Place {house_index} has
# Valentine's day."
# •	If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {house_index} already
# had Valentine's day."
# • Cupid can have a larger jump length than the size of the neighborhood, and if he does jump outside of it, he should
# start from the first house again

neighborhood = list(map(int, input().split("@")))

command = input()
current_index = 0

while command != "Love!":
    command = command.split()
    current_length = int(command[1])
    current_index += current_length
    if current_index >= len(neighborhood):
        current_index = 0

    neighborhood[current_index] -= 2
    if neighborhood[current_index] == 0:
        print(f"Place {current_index} has Valentine's day.")
    elif neighborhood[current_index] < - 1:
        print(f"Place {current_index} already had Valentine's day.")

    command = input()


# In the end, print Cupid's last position and whether his mission was successful or not
print(f"Cupid's last position was {current_index}.")

fails_counter = 0
for x in neighborhood:
    if x > 0:
        fails_counter += 1

if fails_counter > 0:
    print(f"Cupid has failed {fails_counter} places.")
else:
    print("Mission was successful.")

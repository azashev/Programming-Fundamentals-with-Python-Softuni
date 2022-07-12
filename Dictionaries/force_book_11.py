# The force users struggle to remember which side is the different force users from because they switch them too often.
# So you are tasked to create a web application to manage their profiles. You should store information for every unique
# force user registered in the application.

# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"

# The "force_user" and "force_side" are strings, containing any character.


# If you receive "force_side | force_user":
# •	If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# •	Only if there is no such force user in any force side -> add the force user to the corresponding side.
# •	If there is such force user already -> skip the command and continue to the next operation.


# If you receive a "force_user -> force_side":
# •	If there is such force user already -> change their side.
# •	If there is no such force user in any force side -> add the force user to the corresponding force side.
# •	If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# •	Then you should print on the console: "{force_user} joins the {force_side} side!".


# Input / Constraints:
# •	The input comes in the form of commands in one of the formats specified above.
# •	The input ends when you receive the command "Lumpawaroo".

# Output:
# •	As output for each force side, you must print all the force users.
# •	The output format is:
# "Side: {force_side}, Members: {force_users_count}
# ! {force_user1}
# ! {force_user2}
# …
# ! {force_userN}"
# •	In case there are no force users on a side, don't print this side.

forces = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        current_side, current_user = command.split(" | ")
        exist = False
        for side, users in forces.items():
            if current_user in users:
                exist = True
                break

        if not exist:
            if current_side not in forces:
                forces[current_side] = [current_user]
            else:
                forces[current_side].append(current_user)
    elif " -> " in command:
        current_user, current_side = command.split(" -> ")
        for side, users in forces.items():
            if current_user in users:
                forces[side].pop(users.index(current_user))
                break

        if current_side not in forces:
            forces[current_side] = [current_user]
        else:
            forces[current_side].append(current_user)
        print(f"{current_user} joins the {current_side} side!")

for force_side, users in forces.items():
    if len(users):
        print(f"Side: {force_side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")

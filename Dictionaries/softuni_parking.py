# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.

# The program receives 2 types of commands:

# 1: "register {username} {license_plate_number}":
#   • The system only supports one car per user at the moment, so if a user tries to register another license plate using
#   the same username, the system should print:
#   "ERROR: already registered with plate number {license_plate_number}"

#   • If the check above passes successfully, the user should be registered, so the system should print:
#   "{username} registered {license_plate_number} successfully"


# 2: "unregister {username}":
#   • If the user is not present in the database, the system should print:
#   "ERROR: user {username} not found"

#   • If the check above passes successfully, the system should print:
#   "{username} unregistered successfully"


# After executing all commands, print all currently registered users and their license plates in the format:
# •	"{username} => {license_plate_number}"


# Input:
# 1: First line: n - number of commands - integer
# 2: Next n lines: commands in one of the two possible formats:
#   •	Register: "register {username} {license_plate_number}"
#   •	Unregister: "unregister {username}"

# The input will always be valid, and you do not need to check it explicitly.

n = int(input())

parking_lot = {}

for _ in range(n):
    command = input().split()

    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]

        if username not in parking_lot:
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    else:
        username = command[1]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_lot[username]

for user, plate_number in parking_lot.items():
    print(f"{user} => {plate_number}")

# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.

# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

def length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def contains(username):
    is_valid = True
    for ch in username:
        if ch.isalnum() or ch == "_" or ch == "-" and not ch == " ":
            continue
        else:
            is_valid = False
    return is_valid


usernames = input().split(", ")

filtered_users = [user for user in usernames if length(user) and contains(user)]

print('\n'.join(filtered_users))

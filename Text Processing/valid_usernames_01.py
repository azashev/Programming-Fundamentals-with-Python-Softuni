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

def password_validator(password):
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    digits_counter = [x for x in password if x.isdigit()]
    if len(digits_counter) < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    return is_valid


input_password = input()

if password_validator(input_password):
    print("Password is valid")

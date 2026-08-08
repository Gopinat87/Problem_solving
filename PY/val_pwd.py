def validate_password(password):

    if len(password) < 8:
        return "Invalid Password"

    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:

        if ch.isupper():
            has_upper = True

        elif ch.islower():
            has_lower = True

        elif ch.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "Valid Password"

    return "Invalid Password"


password = "Hello123"

print(validate_password(password))
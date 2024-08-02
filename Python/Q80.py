# Program to valid the user's password
# a-z, 0-9, A-Z, $#@, Min(6), Max(12)
# ABd1234@1,aF1#,2w3E*,2We3345


def validate_password(password):
    # Criteria for password validation
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False

    # Check each character in the password
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@!":
            has_special_char = True

    # Check overall validity
    is_valid_length = 6 <= len(password) <= 12
    is_valid_password = has_lowercase and has_uppercase and has_digit and has_special_char and is_valid_length

    return is_valid_password

def main():
    # Input comma-separated passwords
    input_passwords = input("Enter comma-separated passwords: ")
    passwords_list = input_passwords.split(",")

    # Validate each password
    valid_passwords = []
    for password in passwords_list:
        if validate_password(password.strip()):
            valid_passwords.append(password.strip())

    # Print valid passwords
    if valid_passwords:
        print("Valid passwords:", ", ".join(valid_passwords))
    else:
        print("No valid passwords found.")

if __name__ == "__main__":
    main()


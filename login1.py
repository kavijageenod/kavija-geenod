def main():
    print("=" * 50 + "\n")
    print("Welocome to login".center(50) + "\n")
    print("=" * 50 + "\n\n")

def get_username():
    user_name = input("Enter The Username: ")
    return user_name


def get_password():
    password = input("Enter The Password: ")
    return password


def valid_username(user_name):
    if len(user_name) < 3 :
        print("\nToo short username")
        return False
    elif len(user_name) > 10 :
        print("\nToo Long username")
        return False
    elif user_name.isdigit():
        print("\nUsername cannot be only numbers")
        return False
    elif not user_name.isalnum():
        print("\nUsername can only include letters and numbers")
        return False
    elif user_name.isalpha():
        print("\nUsername cannot be only letters")
        return False
    elif user_name.isupper():
        print("\nUser name cannot be in captal form")
        return False

    return True


def valid_password(password):
    if len(password) < 3:
        print("\nToo short password")
        return False   
    elif len(password) > 10:
        print("\nToo Long password")
        return False
    elif password.isalpha():
        print("\nCannot include letters")
        return False

    return True

# main menu
main()

# defined credentials

correct_username = "admin123"
correct_password = "1234"

# Get Inputs

attempt = 3

while attempt > 0 :

    user_name = get_username()
    password = get_password()

    if not valid_username(user_name) or not valid_password(password):
        attempt = attempt - 1
        continue

    elif user_name == correct_username and password == correct_password:
        print("Login Sucessful")
        break

    else:
        print("\nTry Again\n")
        attempt = attempt - 1

if attempt == 0 :
    print("You ran out of attempts")




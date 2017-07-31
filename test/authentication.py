
username_password = {"Bob":"bobiscool"}


def authenticate(login_username, login_password):
    if username_password.get(login_username) is None:
        print("invalid username or password")
    elif username_password.get(login_username) == login_password:
        print(username_password.get(login_username))
        print("welcome back")
    else:
        print("invalid username or password")


print("Sign up for My awesome service!\n")
name = str(input("Please enter your preferred username.\n"))
passcode = str(input("Thank you, now enter a password as well.\n"))
username_password[name] = passcode
print(username_password)

username = str(input("Enter your username.\n"))
password = str(input("Enter your password.\n"))
authenticate(username, password)



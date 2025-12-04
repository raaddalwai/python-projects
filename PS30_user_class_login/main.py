# Create a User class with private password and a method to validate login.

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password

    def validate_login(self, username: str, password: str) -> bool:
        return self.username == username and self.__password == password


def main():
    username = input("Create username: ")
    password = input("Create password: ")
    user = User(username, password)
    attempt_user = input("Username to login: ")
    attempt_pass = input("Password to login: ")
    if user.validate_login(attempt_user, attempt_pass):
        print("Login successful")
    else:
        print("Login failed")


if __name__ == "__main__":
    main()

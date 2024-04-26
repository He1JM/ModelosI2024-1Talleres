"""
This file has a set of classes related to users,
including user privileges.


Author: Henry Osorio - hjosorios@udistrital.edu.co
"""

class AccountManagement:
    def __init__(self):
        self.users = {}

    def authenticate_user(self, username, password, role):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False
        
    def register_user(self, username, password, role):
        if username not in self.users:
            self.users[username] = password
            print("Registration successful!")
        else:
            print("Username already exists. Please choose another username.")
         
class Login:
    def __init__(self):
        self.auth_system = AccountManagement()

    def login(self, username, password, role):
        if self.auth_system.authenticate_user(username, password, role):
            print("Login successful!")
        else:
            print("Login failed. Please check your username and password.")

    def register(self, username, password, role):
        self.auth_system.register_user(username, password, role)


# Example usage
if __name__ == "__main__":
    user = Login()
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            role = input("Enter your role: ")
            user.login(username, password, role)
        elif choice == "2":
            username = input("Enter your desired username: ")
            password = input("Enter your desired password: ")
            role = input("Enter your desired role: ")
            user.register(username, password, role)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
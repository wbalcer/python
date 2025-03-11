class User:
    def __init__(self):
        self.users = {} 

    def register(self, username, password):
        if username in self.users:
            return "Użytkownik już istnieje."
        self.users[username] = password
        return "Sukces."

    def login(self, username, password):
        if username not in self.users:
            return "Niepoprawna nazwa użytkownika lub hasło."
        if self.users[username] == password:
            return "Sukces."
        return "Niepoprawna nazwa użytkownika lub hasło."

user_system = User()
print(user_system.register("testuser", "securepassword"))
print(user_system.login("testuser", "securepassword"))
print(user_system.login("testuser", "wrongpassword"))

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        uname = input("Username: ")
        if uname == self.username:
            pword = input("Password: ")
            if pword == self.password:
                print("Logged in!")
                return True
            else:
                print('login failed')

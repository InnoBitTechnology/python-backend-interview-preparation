class Database:
    def connect(self):
        print('connected!')


class UserService():
    def __init__(self, database):
        self.database = database

    def create_user(self):
        self.database.connect()
        print('User Created!')


database = Database()
userservice = UserService(database)

userservice.create_user()
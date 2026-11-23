class Database:
    def connect(self):
        print("Connected")


class UserService:

    def __init__(self, database):
        self.database = database

    def create_user(self):
        self.database.connect()
        print("User created")

database = Database()
service = UserService(database)

service.create_user()
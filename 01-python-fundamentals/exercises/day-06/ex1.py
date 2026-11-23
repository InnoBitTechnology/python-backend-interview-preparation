class Employee:
    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience
        print(f"My name is {self.name}, I work on {self.role} and I have {self.experience} YOE")


employee = Employee('Mohit', 'BE', 4)
employee2 = Employee('Ramesh', 'FE', 2)

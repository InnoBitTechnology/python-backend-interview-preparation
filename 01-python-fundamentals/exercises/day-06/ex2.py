class Employee:
    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience

    def introduce(self):
        print(f"Hi, I am {self.name}. I work as a {self.role} and have {self.experience} years of experience.")


employee = Employee('Mohit', 'BE', 4)
employee2 = Employee('Ramesh', 'FE', 2)

employee.introduce()
employee2.introduce()
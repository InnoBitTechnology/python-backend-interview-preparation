class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        print(f"I'm {self.name} and i'm in {self.role}")


employee1 = Employee("Manoj", "Backend Developer")
employee2 = Employee("Rahul", "Frontend Developer")

employee1.introduce()
employee2.introduce()
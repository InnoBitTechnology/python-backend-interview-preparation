class Employee:
    def __init__(self, name, role, experience):
        self.name = name
        self.role = role
        self.experience = experience

    def introduce(self):
        print(f"Hi, I am {self.name}. I work as a {self.role} and have {self.experience} years of experience.")

    def calculate_salary(self, basic, hra, da):
        salary = basic + basic*hra/100 + basic*da/100
        print(f"Hi, I am {self.name}. My Gross salary is: {salary}")


employee = Employee('Mohit', 'BE', 4)
employee.calculate_salary(50000, 10, 10)

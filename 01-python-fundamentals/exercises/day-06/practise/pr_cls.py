class Employee:

    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def get_salary(self):
        return self.salary

    # Class method
    @classmethod
    def get_company(cls):
        return cls.company

    # Static method
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

employee = Employee('Mohit', 100000)
print(employee.get_company())

print(Employee.get_company())
print(Employee.is_valid_salary(10000))
print(employee.get_salary())

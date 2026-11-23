class Employee:
    company = "InnoBit"

    @classmethod
    def change_company(cls, company):
            return company

print(Employee.company)
employee1 = Employee()
employee2 = Employee()
print(employee1.change_company("Innobit"))
print(employee2.change_company("IB"))

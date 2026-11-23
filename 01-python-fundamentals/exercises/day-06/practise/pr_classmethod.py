class Employee:

    company = "ABC"

    @classmethod
    def get_company(cls):
        return cls.company


print(Employee.get_company())
class Employee:
    def work(self):
        print("Work")

class Developer(Employee):
    def write_code(self):
        print("Write code")

obj = Developer()
obj.work()
obj.write_code()
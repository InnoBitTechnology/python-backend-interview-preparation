class Employee:
    def work(self):
        print("Employee Working!!")

class Developer(Employee):
    def write_code(self):
        print("Write code")

    def work(self):
        print(f"Developer working!!")

obj = Developer()
obj.work()
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Employee Working!!")

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def write_code(self):
        print("Write code")

    def work(self):
        print(f"Developer working!!")

obj = Developer('Mohit', 'Python')
print(obj.name)
print(obj.language)
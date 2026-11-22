def calculate_salary(basic, hra=20, da=10):
    return basic+(basic*(hra/100))+(basic*(da/100))


print(calculate_salary(basic=int(input("Enter Basic Salary: "))))
print(calculate_salary(basic=int(input()),hra=10, da=40))
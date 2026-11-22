def employee_details(name, role, experience):
    print(f"Name is: {name}")
    print(f"Role is: {role}")
    print(f"Experience is: {experience}")

    

#positional
employee_details('Ram', 'BE', 4)

#keyword
employee_details(name='ram',experience=4,role='BE')
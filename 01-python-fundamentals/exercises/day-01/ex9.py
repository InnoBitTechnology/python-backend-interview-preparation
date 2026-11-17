#basic salary cal
basic_salary = int(input())
HRA = (basic_salary*20)/100
DA = (basic_salary*10)/100

gross_salary = basic_salary + HRA + DA
print(f"Basic: {basic_salary}\nHRA: {HRA}\nDA: {DA}\nGross Salary: {gross_salary}")
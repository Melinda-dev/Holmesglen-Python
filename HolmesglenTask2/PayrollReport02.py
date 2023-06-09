import csv

def Add_employee_to_list(empID, Name, Position, Salary):
    employee = []
    employee.append(empID)
    employee.append(Name)
    employee.append(Position)
    employee.append(Salary)
    return employee


def get_salary(employee):
    print(employee)
    return float(employee[3].replace("\n",""))


#count the line number
employees_file = open("employees.csv", "r")
line_num = 0

filehead = employees_file.readline()
print(filehead)
employees_list = []
employee = []
while filehead is not None:
    employee = employees_file.readline().split(",")
    print(employee)

    if employee == [''] or employee is None:
        break

    employees_list.append(employee)

print(employees_list)
employees_file.close()

# get the salary of different job title
pay_for_manager = 0
pay_for_sales = 0
pay_for_admin = 0

for employee in employees_list:
    if employee[2] == "Manager":
        pay_for_manager += get_salary(employee)
        print(pay_for_manager)
    elif employee[2] == "Sales":
        pay_for_sales += get_salary(employee)
    else:
        pay_for_admin += get_salary(employee)


Total_payroll = pay_for_manager + pay_for_sales + pay_for_admin
Average_pay = Total_payroll / len(employees_list)

number_on_payroll = len(employees_list)

for sub_employees_List in employees_list:
    sub_employees_List[3] = "$" + str(sub_employees_List[3])
    print(* sub_employees_List)


print("Total payroll:", "$", f'{Total_payroll:.2f}')
print("Number on payroll:", f'{number_on_payroll}')
print("Average pay:", "$", f'{Average_pay:.2f}')
print("")
print("Total pay for:")
print("Managers", "$",f'{pay_for_manager:.2f}' )
print("Sales", "$", f'{pay_for_sales:.2f}')
print("Admin", "$", f'{pay_for_admin:.2f}')

with open('PayrollReport.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Total payroll:" , "$"f'{Total_payroll:.2f}'])
    writer.writerow(["Number on payroll:" , f'{number_on_payroll}'])
    writer.writerow(["Average pay:", "$" f'{Average_pay:.2f}'])
    writer.writerow([" "])
    writer.writerow(["Total pay for:"])
    writer.writerow(["Managers", "$" f'{pay_for_manager:.2f}'])
    writer.writerow(["Sales", "$" f'{pay_for_sales:.2f}'])
    writer.writerow(["Admin", "$" f'{pay_for_admin:.2f}'])




def Add_employee_to_list(empID, Name, Position, Salary):
    employee = []
    employee.append(empID)
    employee.append(Name)
    employee.append(Position)
    employee.append(Salary)
    return employee


def get_salary(employee):
    #print(employee)
    return float(employee[3])


#count the line number
employees_file = open("Employees.txt", "r")
line_num = len(employees_file. readlines())
employees_file.close()

# get the employee list from the file
employees_file = open("Employees.txt", "r")
employees_list = []
employee = []
for i in range(0,int(line_num/4)):
    empID = employees_file.readline().replace("\n", "")
    if empID == '':
        break
    Name = employees_file.readline().replace("\n", "")
    Position = employees_file.readline().replace("\n", "")
    Salary = employees_file.readline().replace("\n", "")

    employees_list.append(Add_employee_to_list(empID, Name, Position, Salary))



# get the salary of different job title
pay_for_manager = 0
pay_for_sales = 0
pay_for_admin = 0

for employee in employees_list:
    if employee[2] == "Manager":
        pay_for_manager += get_salary(employee)
        # print(pay_for_manager)
    elif employee[2] == "Sales":
        pay_for_sales += get_salary(employee)
    else:
        pay_for_admin += get_salary(employee)


Total_payroll = pay_for_manager + pay_for_sales + pay_for_admin
Average_pay = Total_payroll / len(employees_list)

number_on_payroll = len(employees_list)


print("Total payroll:", "$", f'{Total_payroll:.2f}')
print("Number on payroll:", f'{number_on_payroll}')
print("Average pay:", "$", f'{Average_pay:.2f}')
print("")
print("Total pay for:")
print("Managers", "$",f'{pay_for_manager:.2f}')
print("Sales", "$", f'{pay_for_sales:.2f}')
print("Admin", "$", f'{pay_for_admin:.2f}')
print("******************")

for sub_employees_List in employees_list:
    sub_employees_List[3] = "$" + str(sub_employees_List[3])
    print(* sub_employees_List)

#creating a text file with the command function "w"

file = open("PayrollReport.csv", "w", newline='')
file.writelines("Total payroll: %s  \n" % f'{Total_payroll:.2f}')
file.writelines("Number on payroll: %s  \n" % f'{number_on_payroll}')
file.writelines("Average pay: %s  \n" % f'{Average_pay:.2f}')
file.writelines("Total pay for:  \n")
file.writelines("Managers %s  \n" % f'{pay_for_manager:.2f}')
file.writelines("Sales %s  \n" % f'{pay_for_sales:.2f}')
file.writelines("Admin %s  \n" % f'{pay_for_admin:.2f}')
file.close()










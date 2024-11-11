employee_table = [
    {'emp_id': 10001, 'emp_name': 'John Smith', 'emp_dept': 'IT', 'emp_salary': 50000.00},
    {'emp_id': 10002, 'emp_name': 'Jane Doe', 'emp_dept': 'HR', 'emp_salary': 45000.00},
    {'emp_id': 10003, 'emp_name': 'Bob Wilson', 'emp_dept': 'IT', 'emp_salary': 55000.00},
    {'emp_id': 10004, 'emp_name': 'Mary Johnson', 'emp_dept': 'FIN', 'emp_salary': 60000.00},
    {'emp_id': 10005, 'emp_name': 'Steve Davis', 'emp_dept': 'HR', 'emp_salary': 48000.00},
]

department_table = [
    {'dept_id': 'IT', 'dept_name': 'Information Tech', 'dept_location': 'New York'},
    {'dept_id': 'HR', 'dept_name': 'Human Resources', 'dept_location': 'Chicago'},
    {'dept_id': 'FIN', 'dept_name': 'Finance', 'dept_location': 'Boston'},
]

emp_dept_table = []

for i in range(len(employee_table)):
    for j in range(len(department_table)):
        if employee_table[i]['emp_dept'] == department_table[j]['dept_id']:
            emp_dept_table.append({
                'comb_emp_id': employee_table[i]['emp_id'],
                'comb_emp_name': employee_table[i]['emp_name'],
                'comb_dept_name': department_table[j]['dept_name'],
                'comb_location': department_table[j]['dept_location'],
                'comb_salary': employee_table[i]['emp_salary']
            })

it_dept_total_salary = 0
hr_dept_total_salary = 0
for employee in employee_table:
    if employee['emp_dept'] == 'IT':
        it_dept_total_salary += employee['emp_salary']
    elif employee['emp_dept'] == 'HR':
        hr_dept_total_salary += employee['emp_salary']

print(f"IT Department Total Salary: {it_dept_total_salary}")
print(f"HR Department Total Salary: {hr_dept_total_salary}")

highest_salary = 0
for employee in employee_table:
    if employee['emp_salary'] > highest_salary:
        highest_salary = employee['emp_salary']

print(f"Highest Salary: {highest_salary}")

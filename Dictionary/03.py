# 3. Create a dictionary with dept no, employee roll no. and salary. 
# Find out department-wise min and maximum of salary.

employees = [
    {'dept_no': 1, 'roll_no': 101, 'salary': 50000},
    {'dept_no': 1, 'roll_no': 102, 'salary': 60000},
    {'dept_no': 2, 'roll_no': 201, 'salary': 70000},
    {'dept_no': 2, 'roll_no': 202, 'salary': 80000}
]

dept_salaries = {}

for emp in employees:
    dept = emp['dept_no']
    salary = emp['salary']
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)

for dept, salaries in dept_salaries.items():
    print(f"Dept {dept} -> Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")

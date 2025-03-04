# calculate net salary 
# where net salary = gross salary + allowance – deduction.
# Allowances are 10% while deductions are 3% of gross salary.

gross = int(input("Enter gross salary : "))
al = gross * (0.1)
de = gross * (0.03)
net = gross + al - de
print(f"Net salary = {net}")

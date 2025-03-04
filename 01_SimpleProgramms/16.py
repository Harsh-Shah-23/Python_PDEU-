# Calculate interest where I = PRN/100.
p = int(input("Enter Principle amount:"))
r = float(input("Enter Rate of interest:"))
t = float(input("Enter time period(in years):"))

i = p*r*t /100
print(f"interest = {i}")

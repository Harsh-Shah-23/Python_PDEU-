# Print factorial of a given number.
a = int(input("Enter any number:"))
fact = 1
i = 1
while (i<=a):
    fact = fact*i
    i+=1
print(f"{a}! = {fact}")
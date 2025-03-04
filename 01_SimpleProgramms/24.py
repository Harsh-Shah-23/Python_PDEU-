# swap two varibles 
a = int(input("Enter any number:"))
b = int(input("Enter another number:"))
print(f"Before swapping, a = {a}, b = {b}")

temp = a
a = b
b = temp

print(f"After swapping, a = {a}, b = {b}")
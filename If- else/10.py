# check preimeter > area or not
l = int(input("Enter length:"))
b = int(input("Enter breadth:"))
p = 2*(l+b)
a = l*b

if (a>p):
    print("Area is greater than perimeter ")
else:
    print("Perimeter is greater than area ")
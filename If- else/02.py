# print the largest and samllest values out of three
a = int(input("Enter a numbers:"))
b = int(input("Enter another number:"))
c = int(input("Enter another number:"))

if(a>b and a>c):
    print(f"{a} is greatest")
elif (b>a and b>c):
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
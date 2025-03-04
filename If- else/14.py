def grade(x):
    y = x // 10  # Use integer division to get whole numbers
    match y:
        case 10 | 9:
            return "O"
        case 8:
            return "O"
        case 7:
            return "A+"
        case 6:
            return "A"
        case 5:
            return "B+"
        case 4:
            return "B"
        case _:
            return "C"
        
a = int(input("Enter marks of subject 1:"))
b = int(input("Enter marks of subject 1:"))
c = int(input("Enter marks of subject 1:"))
t = a+b+c
a = t/3
if (a<=39 or b<=39 or c<=39):
    print("Failed!!")
else:
    print("Passed!!")
print(f"Grade of subjet 1 = {grade(a)}\nGrade of subject 2 = {grade(b)}\nGrade of subject 3 = {grade(c)}")

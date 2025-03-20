# 3. Accept two strings. Check whether one string is there in another string.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 in s2 or s2 in s1:
    print("One string is present in the other.")
else:
    print("No string is found inside the other.")

# A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age

students = [(101, "Alice", 20), (102, "Bob", 21), (103, "Charlie", 22)]
roll_nos = []
names = []
ages = []
for s in students:
    roll_nos.append(s[0])
    names.append(s[1])
    ages.append(s[2])
print(roll_nos)
print(names)
print(ages)

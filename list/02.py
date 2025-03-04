# Generate 20 random integers and store them in a list.
# Accept a number from the user and print position of all occurrences of that number in the list.


import random
lst = []
for i in range(1,21):
    a = random.randint(1,100)
    lst.append(a)
print(lst)
x = int(input("Enter any number in the list : "))

for index,values in enumerate(lst):
    if (x == values):
        print(index)

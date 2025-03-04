# Create a list of 5 odd integers using random nos. 
# Similarly create a list of 4 even integers using random nos.
# Replace the third element of odd integers with  a list of 4 even integers. 
# Flattern, sort and print the list.
# Provide appropriate message at each stage.



lst1 = []
lst2 = []
for i in range(0,5):
    a = int(input("Enter a odd integer :"))
    lst1.append(a)
for i in range(0,4):
    a = int(input("Enter a even integer :"))
    lst2.append(a)
lst1[2] = lst2
print(lst1)


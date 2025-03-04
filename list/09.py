# Take two lists of numbers.
# Create third list of numbers for only those numbers from first list 
# which are not there in 2nd list (use list comprehension). 

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = [x for x in list1 if x not in list2]
print(list3)
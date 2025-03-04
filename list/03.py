# Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.

import random as raand
lst = []
for i in range(1,51):
    a = raand.randint(1,30)
    lst.append(a)
print(lst)

new_lst = list(set(lst))
print(new_lst)
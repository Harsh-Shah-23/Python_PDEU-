# Generate 30 random numbers and put them in a list.
# Create two more lists – one containing only +ve numbers and another with –ve nos.

import random as raand
lst = []
for i in range(1,31):
    a = raand.randint(-100,100)
    lst.append(a)
print(lst)
lst_positive = []
lst_negetive = []

for value in lst:
    if (value > 0):
        lst_positive.append(value)
    else:
        lst_negetive.append(value)

print(f"{lst_positive}\n{lst_negetive}")
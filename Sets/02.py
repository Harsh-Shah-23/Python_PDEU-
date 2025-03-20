# 2. Create a set with 10 random numbers from 15 to 45. 
# Count numbers less than 30 and remove numbers greater than 35.

import random

num_set = {random.randint(15, 45) for _ in range(10)}

count_less_than_30 = sum(1 for num in num_set if num < 30)
num_set = {num for num in num_set if num <= 35}

print("Count < 30:", count_less_than_30)
print("Updated Set:", num_set)

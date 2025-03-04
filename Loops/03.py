# Count no. of alphabets and no. of digits in any given string.
str = input("Enter any string:")
count_digit = 0
count_alpha = 0
i = 0
while (i<len(str)):
    if (str[i].isalpha() == True):
        count_alpha +=1
    if (str[i].isdigit() == True):
        count_digit +=1
    i += 1
print(f"number of digits = {count_digit}")
print(f"number of alphabets = {count_alpha}")

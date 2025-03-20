# 1. Count how many vowels are there in a string. Accept the string from the user.

text = input("Enter a string: ")
vowels = "aeiouAEIOU"

count = sum(1 for char in text if char in vowels)

print("Number of vowels:", count)

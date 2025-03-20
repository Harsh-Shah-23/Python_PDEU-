# 4. Write a program that reads a string from the keyboard and creates 
# dictionary containing frequency of each character occurring in the string.

s = input("Enter a string: ")
char_freq = {}

for char in s:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)

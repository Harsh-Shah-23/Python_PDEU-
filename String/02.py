# 2. Convert all characters of a string into lower case, upper case, and toggle case without built-in functions.

def to_lower(s):
    return "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in s)

def to_upper(s):
    return "".join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in s)

def toggle_case(s):
    return "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in s)

text = input("Enter a string: ")

print("Lowercase:", to_lower(text))
print("Uppercase:", to_upper(text))
print("Toggle case:", toggle_case(text))

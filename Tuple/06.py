# Modify an element of a tuple.

t = (1, 2, 3)
t = t[:1] + (99,) + t[2:]
print(t)

# 4. Separate names starting with A and B into two sets.

names = {"Alice", "Andrew", "Bob", "Barbara", "Alex", "Brian"}

a_names = {name for name in names if name.startswith("A")}
b_names = {name for name in names if name.startswith("B")}

print("A Names:", a_names)
print("B Names:", b_names)

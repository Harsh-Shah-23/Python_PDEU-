# 3. Modify a set by adding five names, updating one, and deleting two.

names = set()

names.update(["Alice", "Bob", "Charlie", "David", "Eve"])
names.discard("Charlie")
names.add("Chris")
names.difference_update(["Alice", "Eve"])

print(names)

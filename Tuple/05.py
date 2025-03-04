# Remove empty tuple(s) from the list of tuples.

lst = [(1, 2), (), (3, 4), (), (5,)]
lst = [x for x in lst if x]
print(lst)

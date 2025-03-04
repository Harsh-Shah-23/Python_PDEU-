# Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.

from datetime import date
d1 = (1, 3, 2024)
d2 = (5, 3, 2024)
date1 = date(d1[2], d1[1], d1[0])
date2 = date(d2[2], d2[1], d2[0])
print(abs((date2 - date1).days))

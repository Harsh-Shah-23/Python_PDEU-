# check weather a point lies inside a circle or not 
from math import sqrt,pow
x = int(input("Enter x - coordinate of circle:"))
y = int(input("Enter y - coordinate of circle:"))
x1 = int(input("Enter x - coordinate of point:"))
y1 = int(input("Enter y - coordinate of point:"))
r = int(input("Enter radius of circle"))

d = sqrt(pow((x-x1),2) + pow((y-y1),2))

if (d<r):
    print("Point lies inside the circle:")
else:
    print("Point lies outside the circle")
    
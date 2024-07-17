# Program to solve Quadratic eqns -> ax2 + bx + c = 0

import math
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

d= (b*b) - (4*a*c)
if d>0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Root 1: {r1}")
    print(f"Root 2: {r2}")
elif d==0:
    r = -b / (2*a)
    print(f"Root: {r}")
else:
    r = -b / (2*a)
    i = math.sqrt(abs(d)) / (2*a)
    print(f"Root 1: {r}+{i}i")
    print(f"Root 2: {r}-{i}i")
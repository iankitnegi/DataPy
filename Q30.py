# Program to calculate natural logarithim of any number

import math
n = float(input("Enter the number: "))

if n<=0:
    print("Please enter the +ve number")
else:
    r=math.log(n, 10)
    print(f"{r} is the logarithim of {n}")
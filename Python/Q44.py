# Program to print Disarium Number 1-100

import math

for i in range(1,101):
    n = i
    s = 0
    c = len(str(n))
    while n>0:
        r=n%10
        s=s+ math.pow(r,c)
        n=n//10
        c=c-1
    if s==i:
        print(i, end=" ")
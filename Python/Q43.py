#Program to check a Disarium Number

s = 0
n = int(input("Enter the number which you want to check: "))
d = n
c = len(str(n))

import math
while n>0:
    r=n%10
    s=s+ math.pow(r,c)
    n=n//10
    c=c-1
if s==d:
    print("DISARIUM NUMBER")
else:
    print("NOT")
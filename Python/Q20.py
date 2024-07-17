#Program to print armstrong number b/w interval

import math 
l = int(input("Enter the lower limit: "))
u = int(input("Enter the upper limit: "))

for i in range(l, u+1):
    L=len(str(i))
    s=0
    d=i
    
    while d>0:
        r=d%10
        s+=r**L
        d=d//10
    
    if s==i:
        print(i)
#Program to check Armstrong Number? 153 = 1^3 + 5^3 + 3^3,  9474 = 9^4 + 4^4 + 7^4 + 4^4

import math
n= int(input("Enter the number: "))
d= n
l= len(str(n))
s=0
r=0

while n>0:
    r=n%10
    s=s+math.pow(r,l)
    n=n//10
    
if d==s:
    print(f"{d} is Armstrong Number")
else:
    print(f"{d} is Not Armstrong Number")

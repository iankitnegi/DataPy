# Program to calculate & print the value according to the given formula Q=Sqrt(2CD/H)   C=50, H=30, D=Input by user -> 100,150,180

import math
C=50
H=30
empty_list=[]
n = input("Enter the numbers: ")
list_ = n.split(',')
for i in list_:
    Q = math.sqrt((2*C*int(i))/H)
    empty_list.append(int(Q))
print(empty_list)

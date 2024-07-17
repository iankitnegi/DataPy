# Program to find LCM

a = int(input("Enter the number 1: "))
b = int(input("Enter the number 2: "))
h = 0
p = a*b

for i in range(1,p):
    if a%i == 0 and b%i==0:
        h=i

print(f"{(a*b)/h} is the LCM of {a} & {b}")
# Program to find factorial of a number

n = int(input("Enter the number: "))
f = 1
for i in range(1, n+1):
    f=f*i
print(f"{f} is the factorial of {n}")
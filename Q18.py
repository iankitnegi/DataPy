#Program to print the Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, ............

a = 0
b = 1
n = int(input("Enter the number of terms: "))
print(a)
print(b)
for i in range(0, n):
    c=a+b
    print(c)
    a=b
    b=c
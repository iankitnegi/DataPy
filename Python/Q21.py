# Program to find the sum of natural numbers: 1, 2, 3, 4, 5, 6, 7 .............

n= int(input("Enter the number: "))
s=0
for i in range(1, n+1):
    s+=i
print("{0} is the final sum".format(s))
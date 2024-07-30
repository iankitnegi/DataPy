# Program to find the number which is divisible by 5&7 b/w 0-100

n=int(input("Enter the number: "))
for i in range(0, n+1):
    if i%5==0 and i%7==0:
        print(i, end=",")
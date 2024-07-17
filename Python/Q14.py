#Program to check Prime Number

n = int(input("Enter the number: "))
c=0

for i in range(1,n+1):
    if n%i==0:
        c=c+1

if c==2:
    print(f"{n} is Prime")
else:
    print(f"{n} is Not Prime")
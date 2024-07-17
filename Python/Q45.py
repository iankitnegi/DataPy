# Happy Number

s = 0
n = int(input("Enter the number which you want to check? "))

while n>9:
    while n!=0:
        r=n%10
        s+=(r**2)
        #print(s)
        n=n//10
    n = s
    s = 0

if n==1:
    print("Happy Number")
else:
    print("Not Happy Number")
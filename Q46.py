# Happy Number b/w 10-100

s = 0
i = 10
while i<=100:
    n=i
    while n>9:
        while n!=0:
            r=n%10
            s+=(r**2)
            n=n//10
        n = s
        s = 0
    if n==1:
        print(i,end=" ")
    i+=1
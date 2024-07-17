# Program to print all prime number b/w 1-10

print("Prime numbers b/w 1-10")
for i in range(1,10):
    z=i
    c=0
    for j in range(1,z+1):
        if z%j==0:
            c=c+1
    if c==2:
        print(z)
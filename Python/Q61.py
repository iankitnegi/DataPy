# Program for removing ith character from a string

str = "Hello, wWorld!"
i = 7
l = len(str)
s = ""
for j in range(0,l):
    if j!=7:
        s=s+str[j]
    else:
        c=str[j]

print(s)
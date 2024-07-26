# Program for find all the duplicate characters

str = "piyush sharma"
l = []
for i in range(len(str)):
    c=-1
    ch = str[i]
    for j in range(len(str)):
        if ch==str[j]:
            c=c+1
    if c>0:
        l.append(ch)

print(list(set(l)))

#Program to split and join a string

str = "Python program to split and join a string"
l = str.split()
print(f"Split String: {l}")

s=""
for i in l:
    s=s+" "+i
print(s.strip())
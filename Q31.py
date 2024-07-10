# Program for cube sum of first n natural numbers

n = int(input("Enter the number: "))
s = 0

for i in range(1, n+1):
    s+=(i**3)
print(f"The cube sum of first {n} natural is {s}")
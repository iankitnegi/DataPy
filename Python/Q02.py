#Program to do addition & division

n1 = int(input("Enter the 1st no.: "))
n2 = int(input("Enter the 2nd no.: "))
s = n1+n2
print(f"sum: {s}")

if n2==0:
    print("Error: Division not possible with 0")
else:
    d=n1/n2
    print(f"division: {d}")
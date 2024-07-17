# Harshad Number. Ex= 18 => 1+8=9 and 18 is divisible by 9

n = int(input("Enter the number which you want to check: "))
d = n
s = 0

while n>0:
    r = n%10
    s = s+r
    n = n//10

if d%s == 0:
    print(f"{d} is Harshad Number")
else:
    print("Not")
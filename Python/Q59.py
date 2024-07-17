# Program to count occ of a element in a list

#Method1
arr = [1,2,3,4,2,5,2,3,4,6,5]
print(f"total length: {len(arr)}")

for i in arr:
    c = 0
    e=i
    for j in arr:
        if e == j:
            c +=1
    print(f"{i} occ in a list: {c}")

#Method2
n = int(input("Enter number which you want to count: "))
c = arr.count(n)
print(f"{n} occ in a list: {c}")
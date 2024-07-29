# Binary search in sorted arr

arr = [10,21,39,42,56,66]
x = int(input("Enter the element which you want to search: "))

f=0
l=len(arr)-1
m=0
pos=0
flag=0

while f<=l:
    m=int((f+l)/2)

    if x<arr[m]:
        l=m-1
    elif x>arr[m]:
        f=m+1
    else:
        pos=m
        flag=1
        break

if flag==1:
    print(f"Element at {pos+1}")
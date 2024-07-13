# Program to split the array and add the first part to the end

arr = [1, 2, 3, 4, 5]
n = int(input("Enter from where you want to split: "))

print(f"Original array: {arr}")
if n<=0 or n>=len(arr):
    print("Not possible")
else:
    f = arr[:n]
    s = arr[n:]
    r = s+f
print(f"Split arr: {r}")
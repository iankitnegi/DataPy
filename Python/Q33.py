# Program to find the largest element in the array

arr = []
print("ENTER 5 ELEMENTS")
for i in range(1,6):
    n = int(input("Enter the number: "))
    arr.append(n)
print(f"{arr} is the array")
print(f"{max(arr)} is the largest number")
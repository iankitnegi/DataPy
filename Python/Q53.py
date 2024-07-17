# Program to find second largest number in list

arr = [30, 10, 45, 5, 20]
arr.sort(reverse= True)
if len(arr)>2:
    print(f"{arr[1]} second largest number in list")
else:
    print("The list doesn't contain second largest number")
# Program to check if given array is Monotonic

def is_monotonic(arr):
    inc = dec = True

    for i in range(1, len(arr)):
        if arr[i]>arr[i-1]:
            dec = False
        elif arr[i]<arr[i-1]:
            inc = False

    return dec or inc

arr1 = [1,2,2,3]
arr2 = [3,2,1]
arr3 = [1,3,2,4]

print("arr1 is monotonic: ", is_monotonic(arr1))
print("arr1 is monotonic: ", is_monotonic(arr2))
print("arr1 is monotonic: ", is_monotonic(arr3))


# Program to find N largest elements from a list

arr = [30, 10, 45, 5, 20, 15, 3, 345, 54, 67, 87, 98, 100, 34]
arr.sort(reverse = True)
# print(arr)

n = int(input("N= "))
print(arr[:n])
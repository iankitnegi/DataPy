# Program to rotate array

arr = [95, 78, 52, 11, 68]
pos = int(input("Enter the position from where you want to rotate an array: "))
l = len(arr)

rra = [0]*l
for i in range(l):
    rra[i]= arr[(pos+i)%l]

print(rra)


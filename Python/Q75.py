# Program which takes 2 disgit no in the form of X,Y & generated a 2D matrix from it

X,Y = input("Enter two digit in X,Y format: ").split(',')

arr = [[0 for j in range(int(Y))] for i in range(int(X))]
print(arr)

for i in range(int(X)):
    for j in range(int(Y)):
        arr[i][j]=i*j

print("Generated Array: ")
for i in range(int(X)):
    for j in range(int(Y)):
        print(arr[i][j], end= " ")
    print("")

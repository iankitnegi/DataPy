# Program to sort words in alphabetic orders

str = input("Enter the string: ")   # suresh ramesh vibhuti gulgule raji ram shyam ajay
list_1 = list(str.split())
list_1.sort()
for i in list_1:
    print(i, end=" ")
# Program to check if a sting is binary/not?

str = input("Enter the string: ")
flag = 0
for i in str:
    if i in "01":
        flag = 1
        
if flag ==1:
    print("Binary")
else:
    print("NOT")

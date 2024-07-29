# Program to find the frequency of the words enter by the user

str = input("Enter the string: ").lower()   # New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3
list_1 = list(str.split())
set_1 = list(set(list_1))

c=0
for i in set_1:
    c=list_1.count(i)
    print(f"{i}={c}")
# Program to make a simple calculator with 4 basic mathematical operation

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

ch = int(input("Enter the choice: 1-Add, 2-Sub, 3-Mul, 4-Div\n"))
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

match ch:
    case 1:
        print(add(x,y))

    case 2:
        print(sub(x,y))

    case 3:
        print(mul(x,y))

    case 4:
        print(div(x,y))

    case _:
        print("Incorrect choice")
    
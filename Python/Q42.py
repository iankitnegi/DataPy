# Program to input a string and print out the text with the uppercase and lowercase letters reversed
# Ex: WelComE TO School -> wELcOMe to sCHOOL

str = input("Enter the string: ")
for i in str:
    c=ord(i)

    if c>=65 and c<=90:
        c=c+32
    elif c>=97 and c<=122:
        c=c-32
    
    print(chr(c), end="")


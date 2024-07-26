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

## Program to do the following operations:
text = "The unexpected always happens"
print(f"\n{text}")

## Length of string
print(f"Length of the str: {len(text)}")

## Check if "pp" present in the string
c = text.find("pp")
if c==-1:
    print("Not Present On The String")
else:
    print("Present")

## Substring from 0 till 10th index
print(text[0:11])

## Replace 'always' with 'never'
print(text.replace("always", "never"))

## Add "no matter what" to the string
print(text+" no matter what")

## Replace all the commas with dots & all dots with commas in the given string
str = "14,625,498.002"
s1 =""
for i in str:
    if i==',':
        s1 += '.'
    elif i=='.':
        s1 += ','
    else:
        s1 += i

print(s1)


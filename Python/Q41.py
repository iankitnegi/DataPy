# Program to remove punctuation from a string

str = input("Enter the string: ")   # Hello!!!, he said ---and went
for i in range(0, len(str)):
    c=ord(str[i])
    if c>=65 and c<=90 or c>=97 and c<=122 or c==32 or c>=48 and c<=57:
        print(chr(c), end="")

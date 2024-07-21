# Program to accept a sentence & calculate the no of letters & digits

str = input("Enter the sentence: ")     #hello World! 123
word_count = 0
digit_count = 0

for i in range(0, len(str)):
     c=ord(str[i])
     if c>=65 and c<=90 or c>=97 and c<=122:
        word_count += 1
     elif c>=47 and c<=56:
         digit_count += 1

print(word_count, digit_count)


#method 2
lc, dc = 0, 0

for char in str:
    if char.isalpha():
        lc +=1
    elif char.isdigit():
        dc +=1

print(lc, dc)







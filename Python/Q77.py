# Program to accept str of space separated words as input & print words after removing all duplicates words and sort them 
# alphanumerically
# Example: hello world and practice makes perfect and hello world again
#=> again and hello makes perfect practice world

str = input("Enter the string: ")
str_set = set(str.split())
new_str=""
for word in sorted(str_set):
    new_str += word+' '

print(new_str)
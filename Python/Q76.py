# Program to sorted comma sep sequence alphabetically. Eg= without,hello,bag,world => bag,hello,without,world

str = input("Enter the string: ")
str_list = str.split(',')
str_list.sort()

new_str=""
for word in str_list:
    new_str += word + ","

for i in range(0,len(new_str)-1):
    print(new_str[i], end="")
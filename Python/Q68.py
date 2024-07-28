#Program to find the sum of all the items in a dictionary
#my_dict = {key:item}

my_dict={
        'a':10,
        'b':20,
        'c':30,
        'd':40,
        'e':50    
}

#Method1:
tot=0
for i in my_dict:
    tot += my_dict[i]
print(tot)

#Method2:
tot=0
for i in my_dict.values():
    tot +=i
print(tot)

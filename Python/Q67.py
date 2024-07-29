# Program to extract unique dctionary values

my_dict={
    'a':10,
    'b':20,
    'c':10,
    'd':30,
    'e':20
}

unique_values = set(my_dict.values())
print(list(unique_values))
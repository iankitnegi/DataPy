# Program to convert key-values list to flat dictionary. Tuple in List => Dict

list_1 = [('a',1), ('b',2), ('c',3), ('d',4)]
flat_dict={}

for k, v in list_1:
    flat_dict[k]=v
print(flat_dict)
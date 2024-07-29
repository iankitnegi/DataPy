# Program to sort Python Dictionaries by VALUE

sample_dict={
    'apple':3,
    'banana':1,
    'date':4,
    'cherry':2
}

sorted_dict_by_values = dict(sorted(sample_dict.items(), key=lambda item:item[1]))
print(sorted_dict_by_values)

for k,v in sorted_dict_by_values.items():
    print(f"{k}:{v}")
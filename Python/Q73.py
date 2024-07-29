# Program to sort Python Dictionaries by KEY

sample_dict={
    'apple':3,
    'banana':1,
    'date':4,
    'cherry':2
}

sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print(sorted_dict_by_keys)

for k,v in sorted_dict_by_keys.items():
    print(f"{k}:{v}")

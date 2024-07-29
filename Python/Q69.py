# Program to merge 2 dictionaries

dict1={
    'a':1,
    'b':2,
    'c':3
}

dict2={
    'd':4,
    'e':5
}

dict1.update(dict2)
print(f"Merged dictionary using .update(): {dict1}")

merged_dict = {**dict1, **dict2}
print(f"Merged dictionary using packing: {merged_dict}")
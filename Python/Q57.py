# Program to remove empty list from list

arr = [[1,2,3], [], [4,5], [], [6,7,8], []]
ne_arr = [i for i in arr if i != []]
print(f"List after removing empty boxs {ne_arr}")
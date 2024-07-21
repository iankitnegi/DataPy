# Program to find words which are greater than given length 'k'

def find_words(word_list, k):
    rslt = []
    for i in word_list:
        if len(i)>k:
            rslt.append(i)

    return rslt

arr = ["apple", "banana", "cherry", "date", "elderberry", "dragonfruit"]
k = int(input("Enter the value of k: "))

print(find_words(arr, k))
# Create a funn that takes a string as input and capitalizes a letter if its ASCII
# is even & returns its lower case version if its ASCII code is odd.
# to be or not to be! => To Be oR NoT To Be!
# THE LITTLE MERMAID => THe LiTTLe meRmaiD

def capitalizes_based_ascii(str):
    new_str=""
    for i in str:
        if ord(i)%2==0:
            new_str=new_str+ i.upper()
        else:
            new_str=new_str+i.lower()
    return new_str

n = input("Enter the string: ")
print(capitalizes_based_ascii(n))
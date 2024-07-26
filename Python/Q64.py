# Program to find the uncommom words from two string

s1 = "This is the first string"
s2 = "This is the second string"

list_s1 = s1.split()
list_s2 = s2.split()
uc_words = ""
for i in list_s1:
    if i not in list_s2:
        uc_words =  uc_words+" "+i

for j in list_s2:
    if j not in list_s1:
        uc_words =  uc_words+" "+j
  
print(uc_words)
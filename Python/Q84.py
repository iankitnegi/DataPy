# Program to generate all the sentences where subjects is in ['I', 'You'] and verb is in ['Play', 'Love'] & 
# the object is in ['Hockey', 'Football']

subjects = ['I', 'You']
verb = ['Play', 'Love']
object = ['Hockey', 'Football']

str=""
arr=[]
for s in subjects:
    for v in verb:
        for o in object:
            str=s+' '+v+' '+o
            arr.append(str)


for a in arr:
    print(a)
# Create a funn to calculate factorial of a number using recursive.

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))
print(fact(6))
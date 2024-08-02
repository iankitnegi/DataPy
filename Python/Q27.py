# Fibonacci Seq using Recursion 

def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
    
nterms = int(input("Enter the no of terms: "))

if nterms<=0:
    print("Please. Enter the positive number")
else:
    print("Fibonacci Seq: ")
    for i in range(nterms):
        print(fibonacci(i))
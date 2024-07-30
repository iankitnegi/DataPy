# Program to print the even number 0-n in comma separated form while n is input by console

def even_numbers(fn):
    for i in range(0,n+1):
        if i%2==0:
            yield i

try:
    n = int(input(("Enter the number: ")))
    r = even_numbers(n)
    print(','.join(map(str,r)))
except ValueError:
    print("Invalid number!")
finally:
    print("THE END")

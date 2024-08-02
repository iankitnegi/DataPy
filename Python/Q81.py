# Define a class with a generator which can iterate the numbers, which is divisible 
# are divisible by 7 b/w a given range 0-n

## yield 

class DivisibleBy7:

    def __init__(self,n) -> None:
        self.n=n

    def generator_divisiblebySeven(self):
        for i in range(self.n):
            if i%7==0:
                print(i)

l = int(input("Enter the limit: "))
D1 = DivisibleBy7(l).generator_divisiblebySeven()
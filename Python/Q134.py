# Create a Constr named called Circle that create a radius provided 
# an argument. The circle constructed must have two getters getArea()
# & getPerimter()

import math

class Circle:
    def __init__(self, r) -> None:
        self.radius = r

    def getArea(self):
        return round (math.pi * self.radius **2)
    
    def getPerimeter(self):
        return round(2* math.pi *self.radius)
    
A = Circle(11)
print(A.getArea())
print(A.getPerimeter())

B = Circle(4.44)
print(B.getArea())
print(B.getPerimeter())


        
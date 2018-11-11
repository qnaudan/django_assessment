import math

class circle:
    def __init__(self, r):
        self.radius=r
    def perimeter(self):
        return(2*math.pi*self.radius)
    def area(self):
        return(math.pi*self.radius**2)

C = circle(2.56)
print('Perimeter = ', C.perimeter(), ' / Area = ', C.area())
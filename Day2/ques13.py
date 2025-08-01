# Circle Class for Area and Perimeter

# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.


import math
class circle :
    def __init__(self,radius) :
        self.radius =  radius
    def area (self) :
        return math.pi * self.radius * self.radius
    def perimeter (self) :
        return 2 * math.pi * self.radius

r = int(input("Enter radius: "))
circle1 = circle(r)
print(circle1.area())
print(circle1.perimeter())
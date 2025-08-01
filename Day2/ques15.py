# Shape Class with Subclasses for Different Shapes

# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.


import math
class shape:
    def area (self):
        pass
    def perimeter (self):
        pass

class circle (shape):
    def __init__(self,radius) :
        self.radius =  radius
    def area (self) :
        return math.pi * self.radius * self.radius
    def perimeter (self) :
        return 2 * math.pi * self.radius
    
class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side
    
class triangle(shape):
    def __init__(self,s1,s2,s3,base,height):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.base = base
        self.heigth = height
    def area(self):
        return 0.5 * self.base * self.heigth
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
rad = int(input("Enter radius: "))
c = circle(rad)
print(f"Area of circle is {c.area()}")
print(f"Perimeter of circle is {c.perimeter()}")

side = int(input("Enter side of square: "))
sq = square(side)
print(f"Area of sqaure is {sq.area()}")
print(f"Perimeter of sqaure is {sq.perimeter()}")
        
s1 = int(input("Enter first side of triangle: "))
s2 = int(input("Enter second side of triangle: "))
s3 = int(input("Enter third side of triangle: "))
b = int(input("Enter base of triangle: "))
h = int(input("Enter height of triangle: "))
tri = triangle(s1,s2,s3,b,h)
print(f"Area of triangle is {tri.area()}")
print(f"Perimeter of triangle is {tri.perimeter()}")
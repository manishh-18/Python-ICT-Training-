# Calculator Class for Basic Arithmetic Operations

# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.


class operations :
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add (self) :
        return self.num1 + self.num2
    def sub (self) :
        return self.num1 - self.num2 
    def multiply (self) :
        return self.num1 * self.num2 
    def div (self) :
        return self.num1 / self.num2 

n1 = int(input("Enter first num: "))
n2 = int(input("Enter first num: "))
arth = operations(n1,n2)
print(arth.add())
print(arth.sub())
print(arth.multiply())
print(arth.div())
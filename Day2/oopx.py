'''
    OOPs :-
        - Class
        - Object 

        - Abstraction
        - Encapsulation
        - Inheritance
        - Polymorphism
'''


# Making class 
class class1 :
    def __init__(self): # Here self refers to the current object
        pass
    id = 1
    name = "Manish"

# # Making object 
# obj = class1()

# Inheritance
class class2(class1):
    email = "manish@gmail.com"

obj = class2()
print(obj.name)


# Multiple inheritance
class user :
    name = "Manish"
    password = 123

class student :
    id = 1
    dept = "CSE"

class teacher(user,student) :
    subject = "Python Programming"
    
obj1 = teacher()
print(obj1.dept)


# Multilevel inheritance
class A:
    name = "Manish"
class B(A):
    id = 1
class C(B):
    password = 123

obj3 = C()
print(obj3.name)



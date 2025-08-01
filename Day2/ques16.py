# Stack Data Structure Class

# Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.


class stack:
    def __init__(self):
        self.items = []
    def push(self,el):
        self.items.append(el)
        print(f"{el} is pushed into the stack") 
    def pop(self):
        if not self.is_empty():
            print(f"{self.items.pop()} is popped from the stack") 
        else:
            print("You cannot pop from empty stack") 
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        print(f"Size of the stack is {len(self.items)}")

s1 = stack()
s1.push(1)
s1.push(3)
s1.push(4)
s1.push(5)
s1.pop()
s1.size()
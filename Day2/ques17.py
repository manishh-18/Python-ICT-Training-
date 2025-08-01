# Shopping Cart Class

# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.



class shoppingCart:
    def __init__(self):
        self.items = []
    def addItem(self,itemName,qnty):
        item = (itemName,qnty)
        self.items.append(item)
    def removeItem(self,item):
        

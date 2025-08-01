# Handle ZeroDivisionError Exception

# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.


def divide(n,d):
    try:
        print(n/d)
    except ZeroDivisionError:
        print("You cannot divide a number with zero")

n = int(input("Enter numerator: "))
d = int(input("Enter denomerator: "))
divide(n,d)
# Maximum of Three Numbers

# Write a Python function to find the maximum of three numbers.

def max(a,b,c):
    if a > b and a > c:
        print(f"{a} is maximum")
    elif b > a and b > c:
        print(f"{b} is maximum")
    else:
        print(f"{c} is maximum")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
max(a,b,c)
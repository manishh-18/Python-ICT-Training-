# Cubes Generator

# Write a Python program that creates a generator function that yields cubes of numbers from 1 to n. Accept n from the user.


def cube(num):
    i = 1
    while i <= num:
        yield i*i*i
        i += 1

n = int(input("Enter number: ")) 
print(f"Cubes of numbers from 1 to {n} are") 
for i in cube(n):
    print(i)
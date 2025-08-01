# Function Lambda Generator

# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75


def func (n) :
    return lambda x : x * n

result1 = func (2)
print(f"Double the number of 15 = {result1(15)}")
result2 = func (3)
print(f"Triple the number of 15 = {result2(15)}")
result3 = func (4)
print(f"Quadruple the number of 15 = {result3(15)}")
result4 = func (5)
print(f"Quintuple the number of 15 = {result4(15)}")
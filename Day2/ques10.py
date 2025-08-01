# Factorial of a Number

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


def fact(num):
    if num == 0 :
        return 1
    else :
        return num * fact (num - 1)

print(fact(5))
# Create a Decorator to Measure Function Execution Time

# Write a Python program to create a decorator function to measure the execution time of a function.


import time

def measure_execution_time(func):
    def wrapper(*a,**ka):
        start = time.time()
        result = func(*a,**ka)
        end = time.time()
        execution_time = end - start
        print(f"Execution of {func.__name__} is {execution_time:.4f} seconds")
        return f"Result: {result}"
    return wrapper

@measure_execution_time
def total(num):
    tot = 0
    for i in num:
        tot += i
    return tot

print(total([1,2,3,4,5,1,2]))
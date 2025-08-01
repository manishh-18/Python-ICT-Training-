# Random Number Generator

# Write a Python program to implement a generator that generates random numbers within a given range.


import random
def random_num_generator(start,end):
    i = 0
    while i < 50:
        yield random.randint(start,end)
        i += 1

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Random numbers from {start} to {end} are:")

randomNums = random_num_generator(start,end)
for i in randomNums:
    print(i)

# Sum All Numbers in a List

# Write a Python function to sum all the numbers in a list.


def sum(*l):
    total = 0
    for num in l:
        total += num
    print(total)

sum(1,2,3,4,5)
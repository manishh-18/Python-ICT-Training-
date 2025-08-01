# Multiply All Numbers in a List

# Write a Python function to multiply all the numbers in a list.


def sum(*l):
    pro = 1
    for num in l:
        pro *= num
    print(pro)

sum(1,2,3,4,5)
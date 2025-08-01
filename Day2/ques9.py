# Reverse a String

# Write a Python program to reverse a string.


def reverseStr(s):
    length = len(s)
    rstr = ""
    while length > 0:
        rstr += s[length-1]
        length -= 1
    print(rstr)

reverseStr("Manish")
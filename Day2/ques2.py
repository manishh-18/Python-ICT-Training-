# Get string of first and last 2 chars.

# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

s_str = input("Enter string: ")
if len(s_str) < 2:
    print("Empty string")
else:
    new_str = s_str[:2] + s_str[len(s_str)-2:]
    print(new_str)

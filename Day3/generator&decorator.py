
# Generator :=

def asdf(a):
    i = 0
    while i <= a:
        yield i # Here yield store all the output in the form of collection (temporary memory) and return us the value when we needed
        i += 1
    
for i in asdf(5):
    print(i)



# Decorator :-

def dec(func):
    def wrapper(*a,**ka):
        print("Anything")
        a = func(*a,**ka) + 3
        return a
    return wrapper

@dec
def asdf():
    return 3 + 4

print(asdf())
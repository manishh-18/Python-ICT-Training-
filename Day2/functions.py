'''
Types of functions:-
    - Built in
    - User defined
        Types of parameter -
            - Default
            - keyword
            - Multivalue
            - Key word multivalue
    - Anonymous (lemda function)
    - Higher order
        - Generator
        - Decorator
'''

def func1(*a):
    print(type(a))

func1(1,2,3,4) # Here type will be tuple


def func2(**a):
    print(type(a))
func2(a=1,b=2,c=3) # Here type will be dictionary because of mapping


'''
    Lemda function
    Syntax :- 
        var = lambda<para>: code block 
    This function is called using its variable name in which it is stored
    Syntax :-
        var(parameters)
'''


'''
    Decorator :-
        @func_B
        func_A : # Simple function
            a+b
        func_B : # Decorator which enhance the functionality of func_A
            func_A + c
            
'''
# Python Decorators
# -----------------------------------
# A decorator takes in a function, adds some functionality and
#  returns it.

# Functions can be passed as arguments to another function.
# Such functions that take other functions as arguments are also 
# called higher order functions. 
# Basically, a decorator takes in a function, adds some
#  functionality and returns it.


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")
ordinary()
ordinary=make_pretty(ordinary)
ordinary()

# The function ordinary() got decorated and the returned 
# function was given the name ordinary 
# Generally, we decorate a function and reassign it as older



# We can use the @ symbol along with the name of the decorator
#  function and place it above the definition of the function
#   to be decorated.

@make_pretty
def ordinary():
    print("I am ordinary")

# is equivalent to

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)    

# Decorating Functions with Parameters
#----------------------------------------------------

def smartdev(func):
    def inner(a,b):
        if(a<b):
            a,b=b,a
            print(a/b)
        else:
            func(a,b)
    return inner

@smartdev
def div(a,b):
    print(a/b)

div(10,15)
div(15,10)
       
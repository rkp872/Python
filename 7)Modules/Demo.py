#Modules in Python
#-------------------------------------------------------
# Modules refer to a file containing Python statements and 
# definitions.

# A file containing Python code, for example: example.py, is
#  called a module, and its module name would be example.

# We use modules to break down large programs into small manageable
#  and organized files. Furthermore, modules provide reusability 
#  of code.

# We can import the definitions inside a module to another module.
# We use the import keyword to do this.

import Calc as c

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

res=c.add(a,b)
print("Sum is : ",res)

res=c.sub(a,b)
print("Difference is : ",res)

res=c.mul(a,b)
print("Product is : ",res)

res=c.div(a,b)
print("Quotient is : ",res)





#Different Types of import statements
#------------------------------------------------------
#WAY 1  :   Python import statement
#-------------------------------------------------------

# We can import a module using the import statement and access
#  the definitions inside it using the dot operator

# to import standard module math

# import math
# print("The value of pi is", math.pi)

#-------------------------------------------------------
#WAY 2  :   Import with renaming
#----------------------------------------------------

# We can import a module by renaming it as follows:

# import module by renaming it

# import math as m
# print("The value of pi is", m.pi)

# We have renamed the math module as m. This can
#  save us typing time in some cases.

# Note that the name math is not recognized in our scope. 
# Hence, math.pi is invalid, and m.pi is the correct implementation.

#-------------------------------------------------------
#WAY 3  :   Python from...import statement
#----------------------------------------------------
# We can import specific names from a module without importing the module as a whole. Here is an example.

# import only pi from math module

# from math import pi
# print("The value of pi is", pi)

# Here, we imported only the pi attribute from the math module.

# In such cases, we don't use the dot operator. 

#-------------------------------------------------------
#WAY 4  :   Import all names
#----------------------------------------------------
# We can import all names(definitions) from a module using the following construct:

# import all names from the standard module math

# from math import *
# print("The value of pi is", pi)

# Here, we have imported all the definitions from the math module. 
#---------------------------------------------------------------------------------------------
#Arrays are collection of similar type elements.
#Arrays can be used after importing array module

from array import *

# since array can contain only homogeneous data so , for declaring the type of array we have to use typecode

#TYPECODE   TYPE
#---------------------
# 'b' : signed char
# 'B' : unsigned char
# 'u' : Py_UNICODE
# 'h' : signed short
# 'H' : unsigned short
# 'i' : signed int
# 'I' : unsigned int
# 'l' : signed long
# 'L' : unsigned long
# 'q' : signed long long
# 'Q' : unsigned long long
# 'f' : float
# 'd' : double


val=array('i',[110,-32,52,69,12]) # Syntax of array creation
print(val)

# val=array('I',[2,-96,3,4,5,6])    Unsigned int array cannot store negative integer,It will generate error
# print(val)

print(val.buffer_info())    # used to obtain the base address of the array and size of array

print(val[0])   # elements can be accessed by index

# ACccessing elements  one by one  using loop

for i in val:
    print(i)

for i in range(len(val)):
    print(val[i])





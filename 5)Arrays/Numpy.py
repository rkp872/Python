# NumPy is a python library used for working with arrays.
# It also has functions for working in domain of linear 
# algebra, fourier transform, and matrices.

from numpy import *

#Different ways of creating Numpy Arrays
#-----------------------------------------
# Using numpy.array()
# Using arange() function
# Using linspace() function
# Using logspace() function
# Using  ones()
# Using zeros()



# Using numpy.array()
#------------------------
#Arrays can be created by passing a list to the function numpy.array()

arr=array([2,3,6,9,5,8.6,3.6])
print(arr.dtype)    # Tells the type of array and size of one element(in bits)
print(arr)

#We can also specify type of array while creating it
arr=array([2,3,6,9,5,8.6],int)
print(arr.dtype)
print(arr)


# Using arange() function
#-------------------------------
# The arange() function is one of the Numpy's most
# used method for creating an array within a specified
# range. The first argument takes the starting point
# of the array you want to create, second is the stop
# point and the third is the step (just like python list
# slicing function). The last argument is again dtype,
# which is optional.

#arange(start, end, step, dtype)
#Among all of the arguments only end is mandatory and by
# default start=0 and step=1. Let's take a few examples,

arr=arange(5,25,2,int)
print(arr)

arr=arange(20)
print(arr)


# Using linspace() function
#----------------------------------

# Imagine if you have some arguments in arange() function
#  to generate a Numpy array, which gives you the output
#   array that has elements not linearly stepped, in such 
#   a case, linspace() comes to the rescue.
# linspace() function takes arguments: start index, end
#  index and the number of elements to be outputted.
#   These number of elements would be linearly spaced 
#   in the range mentioned.

# linspace(start_index, end_index, num_of_elements)
arr=linspace(15,75,10)
print(arr)


# Using logspace() function
#-------------------------------
#similar to linspace but here the items
#  will not be lineraly splaced but logarithmic spaced
arr=logspace(10,36,20)
print(arr)

# Using  ones()
#----------------------
# create array full of ones
arr=ones(10,int)
print(arr)



# Using  zeros()
#----------------------
# create array full of ones
arr=zeros(10,int)
print(arr)


#  Numpy arrays can have more than one dimension.

import numpy as np

arr1=np.array([
    [1,2,3,4],
    [11,12,13,14],
    [21,22,23,24]
])
print(arr1)

print(arr1.ndim)    # Print the Dimentions of array 

print(arr1.size)    #Print the size of the array

# Another way to create 2D array is to start
# with a 1-dimensional array and use the
# numpy reshape() function that rearranges
# elements of that array into a new shape.

a = np.array([1, 2, 3, 4, 5, 6])
b=np.reshape(a,(2,3))   # a: the array to be reshaped       
                         #  (2,3) : dimensions of the new array 
print(b)

# b is a 2-dimensional array, with 2 rows and 3 columns. 
# We can access its elements by specifying row and column
#  indexes

print(b[0,2])   # get the element in  0-th row and 2-nd column

b[0,2] = 100
print(b)


# Mathematical operations on multidimensional arrays
#-----------------------------------------------------
a=np.arange(4)
b=np.reshape(a,(2,2))
print(b)

c=10*b   # multiplication by a number
print(c)

d=b+c   # addition of two arrays of the same dimensions
print(d)

e=b*c   ## multiplication of two arrays of the same dimensions
print(e)

# Notice that array multiplication multiplies 
# corresponding elements of arrays.

#  In order to perform matrix multiplication of 2-dimensional arrays
#   we can use the numpy dot() function

f=np.dot(b,e)   # matrix multiplication of b and e
print(f)

# Mathematical functions defined by numpy 
# can be applied to multidimensional arrays

print(np.max(f))
print(np.min(f))
print(np.cos(f))
print(np.log(f))

#Slicing multidimensional arrays
#------------------------------------

a = np.reshape(np.arange(30), (5,6)) # create a 5x6 array
print(a)

# In order to create a slice of a multidimensional array
#  we need to specify which part of each dimension
#   we want to select.

b=a[1:4,0:2]    #select elements in rows 1-3 and columns 0-1
print(b)

c = a[:3, 2:4] #select elements in rows 0-2 and columns 2-3
print(c)

d = a[:, 0] # select all elements in the 0-th column
print(d)


# we can convert 2d array in 1d array by using flatten() function

b=a.flatten()   # 1d array will be created
print(b)


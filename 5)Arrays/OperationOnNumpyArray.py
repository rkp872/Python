import numpy as np
#  Numerical operations on numpy arrays

#Elementwise operations
#--------------------------

#With scalars:
arr=np.array([1,2,3,4])
print(arr+1)

print(2**arr)

#All arithmetic operates elementwise:

arr2=np.ones(4,int)+1
print(arr2)
print(arr+arr2) #in this case number of elements in both arrays must be same
print(arr-arr2)
print(arr*arr2)
print(arr / arr2)
print(arr % arr2)
print(np.sqrt(arr2))

#Comparisons:
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a==b)
print(a>b)

#Logical operations:
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))

#Transcendental functions:
a = np.arange(5)
print(np.sin(a))
print(np.log(a))

#Shape mismatches
# a = np.arange(4)
# a + np.array([1, 2]) 
        # Exception has occurred: ValueError
        # operands could not be broadcast together with shapes (4,) (2,) 

#Basic reductions
# -----------------------

# Computing sums
x = np.array([1, 2, 3, 4])
print(np.sum(x))

#Extrema:
x = np.array([1, 3, 2])
print(np.max(x))

print(np.min(x))
print(np.argmin(x)) # index of minimum
print(np.argmax(x)) # index of maximum

#Statistics:
x = np.array([1, 2, 3, 1])
print(np.mean(x))
print(np.median(x))
print(np.std(x))    # full population standard dev.

# Sorting data
x = np.array([1, 2, 3, 1])
x=np.sort(x)
print(x)

#--------------------------------------------
#COPYING CONTENT OF ONE ARRAY TO ANOTHER
#------------------------------------------
#we can copy content of array in three ways
#---------------------------------------------
# 1: WAY 1      : Assignment Operator
#---------------------------------------------
a=np.array([10,20,30,40,50])
b=a
print(b)
# this will not create new array but
#  only reference will be created and will
#  point to the same memory location
# we can check it using id()
print(id(a))
print(id(b))    # same id will be printed for both

#------------------------------------
# 2: WAY 2      : Shallow copy
#------------------------------------

a=np.array([10,20,30,40,50])
b=a.view()
print(b)

# separate array will be created 
# at another meemory Location
#this is called as swallow copy

# The copying process does not recurse and
# therefore won’t create copies of the child
# objects themselves. In case of shallow copy,
# a reference of object is copied in other object.
# It means that any changes made to a copy of object
# do reflect in the original object.


print(id(a))
print(id(b))    # different id will be printed for both

#------------------------------------
# 3: WAY 3      : Deep copy
#------------------------------------
a=np.array([10,20,30,40,50])
b=np.copy(a)
print(b)


# In case of deep copy, a copy of object is copied
#  in other object. It means that any changes made
#   to a copy of object do not reflect in the
#    original object.

print(id(a))
print(id(b))     # different id will be printed for both





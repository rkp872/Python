#The 2-dimensional array (2D array)
#------------------------------------------
# Two dimensional array is an array within an array.
#  It is an array of arrays.

from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]


# The data elements in two dimesnional arrays can be 
# accessed using two indices. One index referring to
#  the main or parent array and another index referring 
#  to the position of the data element in the inner array.


print(T[0])
print(T[1][2])


# To print out the entire two dimensional array we can use python for loop

for r in T:
    for c in r:
        print(c,end=" ")
    print()

#We can insert new data elements at specific position 
# by using the insert() method and specifying the index.

T.insert(2,[36,54,85,69])

for r in T:
    for c in r:
        print(c,end=" ")
    print()

# We can update the entire inner array or some specific 
# data elements of the inner array by reassigning the values 
# using the array index.

T[2]=[10,20]
T[0][3] = 7
print()
print()
for r in T:
    for c in r:
        print(c,end=" ")
    print()


# We can delete the entire inner array or some specific data
#  elements of the inner array by reassigning the values using
#   the del() method with index. 

del(T[1])
print()
print()
for r in T:
    for c in r:
        print(c,end=" ")
    print()















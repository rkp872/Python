# In Python, an anonymous function is a function that is defined
#  without a name.
# While normal functions are defined using the def keyword
#  in Python, anonymous functions are defined using the lambda
#   keyword.
# Hence, anonymous functions are also called lambda functions.

# Syntax of Lambda Function in python
#------------------------------------
# lambda arguments: expression
#------------------------------------

# Lambda functions can have any number of arguments but only one
#  expression. The expression is evaluated and returned. 

double=lambda x : x*2
print(double(5))

#We use lambda functions when we require a nameless
#  function for a short period of time.



# Lambda functions are used along with built-in functions
#  like filter(), map() etc.

# use with filter()
# ------------------------------------------

# The filter() function in Python takes in a function and a list
#  as arguments.

# The function is called with all the items
#  in the list and a new list is returned which contains
#   items for which the function evaluates to True.

# Here is an example use of filter() function to filter
#  out only even numbers from a list.

# Program to filter out only the even items from a list
myList = [1, 5, 4, 6, 8, 11, 3, 12]
newList=list(filter(lambda x : x%2==0 ,myList))
print(newList)


# use with map()
#-------------------------------------------
# The map() function in Python takes in a function and a list.

# The function is called with all the items in the list and a new
#  list is returned which contains items returned by that function for each item.

# Here is an example use of map() function to double all
#  the items in a list.

myList=[1,5,4,6,8,11,12,3]
newList=list(map(lambda x : x*2,myList))
print(newList)



# Use of lambda() with reduce()
#----------------------------------------------------

# The reduce() function in Python takes in a function and a list
#  as argument. The function is called with a lambda function
#   and a list and a new reduced result is returned. 

from functools import reduce
myList=[5,8,10,20,50,100]
sum=reduce(lambda x,y : x+y ,myList)
print(sum)
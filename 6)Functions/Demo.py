# Function blocks begin with the keyword 
# def followed by the function name and parentheses ( )

def Greet():    
    print("Hello")
Greet() # Calling Greet function




# Python Argument Passing model
#-------------------------------------

# Everything in Python is an object.
# all objects in Python can be either mutable or immutable.
# Objects of built-in types like
#  (int, float, bool, str, tuple, unicode) are immutable. 
#  Objects of built-in types like (list, set, dict) are mutable. 
#  Custom classes are generally mutable. 

# Python’s argument passing model is neither “Pass by Value” nor
#  “Pass by Reference” but it is “Pass by Object Reference”.


#  In the event that you pass immutable arguments like whole numbers, 
#  strings or tuples  to a function, the passing is like 
#  call-by-value because you can not change the value of the
# immutable objects being passed to the function.

string="Rohit"
def test(string):
    #here string referes to same memory location as the caller string
    print((id(string)))
    string="Rohit Pandey"
    #since value of immutable object is updated so new memory will be allocated to string here
    print((id(string)))
    print("Inside Function : ",string)
print((id(string)))
test(string)    #It is like call by value  because we are passing immutable object (string)
print("Outside function : ",string)

#  Whereas
#  passing mutable objects can be considered as call by reference
# because when their values are changed inside the function,
# then it will also be reflected outside the function.

def addMore(list):
    list.append(50)
    print("Inside function : ",list)
myList=[10,20,30,40]
addMore(myList) #It is like call by reference since we are passing mutable object list
print("Outside function : ",myList)






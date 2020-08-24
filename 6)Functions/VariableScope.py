#The location where we can find a variable and also access it if required is
#  called the scope of a variable.
# In python we can have global or local scopes

# GLOBAL SCOPE: 
#---------------------
# Variables which are declared from outside the function i.e. from driver area, has global scope.
# That is they can be accessed from driver area as well as from any functions. 


#LOCAL SCOPE :  
#-----------------
# Variables which are declared from inside some function has local scope.That is they can be accessed from
# only inside that function and not from any other function or driver area

a=10    #Global variable a
def fun():
    a=15    #Local Variable a
    print("Inside fun ", a)
fun()
print("Outside ", a)

#Accessing global variable inside the function
#----------------------------------------------------
#Inside the function if we dont have any variable with the same name ,
#then we can acess it directly 

a=10    #Global variable a
def fun():
    print("Inside fun ", a) # Accessing global variable a in fun
fun()
print("Outside ", a)

# But in this case we can only acessing the value of the variable but cannot 
# Change the value.As we try to change the value,a new local variablw will be created with the same name

a=10    #Global variable a
def fun():
    a=15    #Trying to change the value of global variable 
            #But it will create a local variable a
    print("Inside fun ", a) # Accessing global variable a in fun

fun()
print("Outside ", a)

# So in this case we have to use a keyword global to specify that 
# I am using global variable 

a=10    #Global variable a
def fun():
    global a
    a=15    #Updating global variable a 
    print("Inside fun ", a)
fun()
print("Outside ", a)

# But again now,here we cannot create another local variable with the same name a
# As the word a is now reserved for global a


# So if we have a variable with same name in the function as in the global one
# We have the best solution to use a funtion globals() which gives you the access of all the global variable 

a=10    #Global variable a
b=20
c=30
def fun():
    a=5
    x=globals()['a']    # globals() gives all the globals variables at once .So we have to provide the name of the variable we want using a square bracket    
    print("Inside fun ", a) 
    print("Value of global a ",x) 
    globals()['a']=25
    print("After Updation in function : ",x)
fun()
print("Outside ", a)


# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside
# the parentheses.

#In python we have different types of agruments: 
# 1 : Position Argument
# 2 : Keyword Argument
# 3 : Default Argument
# 4 : Variable length Argument 
# 5 : Keyworded Variable length Argument 


#-------------------------------
# 1 : Position Argument

# while calling the function ,order of  passing the values is important
#because the values will be binded with the formal argument in the same order
#this types of argument is called as positional argument

def person(name,age):
    print("Name is: ",name)
    print("Age is : ",age)
name="Rohit"
age=23
person(name,age)
#person(age,name)   This is not the correct way because 23 will go to name and rohit will go to age in the function

#---------------------------------
# 2 : Keyword Argument

#Many a times the function is defined by some other people and is used by some other people.
#So the caller doesn't know the formal agrument order
#In this case keyword argument can be used where we use the keyword with the 
# arguments while caling it

def person(name,age):
    print("Name is: ",name)
    print("Age is : ",age)
name="Rohit"
age=23
person(age=age,name=name)

#--------------------------------------------------
# 3 : Default Argument

#Sometimes caller doesn't provide all the values for the formal argument
#In this case while defining the funtion only we can provide default value for the argument whose value will not be passed by caller
#This type of argument is called default argument

def person(name,age=18):
    print("Name is: ",name)
    print("Age is : ",age)
name="Rohit"
person(name)
#------------------------------------------
# 4 : Variable length Argument 

#sometimes caller may paas more number of arguments than the number of formal agruments
#In that case the formal arguments must be of variable length
# we can create variable length argument by putting * sign before the name of last argument

def sum(a,*b):      
    sum=a
    for i in b:     #In the funtion all the passed value will be stored in a tuple with name b,So for accessing it we have to use for loop here
        sum=sum+i
    print("Sum is ",sum)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40,50,60,40)
#-----------------------------------------------------------
# 5 : Keyworded Variable length Argument 

# Foe having meaningful use of the variable length arguments we can also
# specify a keyword with them while passing ,which denotes the what data 
# it is storing .Such type of arguments  are called as 
#Keyworded Variable length Argument 

def person(name,**data):
    print(name)
    for i,j in data.items():    #Foe accessing one data at a time we use item() function
        print(i,j)

person("Rohit",age=25,city="Ranchi",Mobile=9123114708)

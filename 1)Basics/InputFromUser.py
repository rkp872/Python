#Taking integer value from user
x=int(input("Enter a number: ")) # By default accepted value is considered as string 
                                # so we convert it into int
y=int(input("Enter another number: "))
z=x+y
print(z)


#If we need to take only first charecter entered by user
ch=input("Enter a charecter : ")[0]
print(ch)


#eval() method can be used for eveluating any mathematical operation
x="2+3+6+7+9*2-32"
res=eval(x)
print(res)

#We can use eval to solve expression given by the user in input
result=eval(input("Enter an expression : "))
print(result)



#Command Line Argument
#there is an array argv which stores all the argument passed through command line
#argv is present in sys module so me must import that module

import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=x+y
print(z)

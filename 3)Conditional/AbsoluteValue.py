# Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1

value=int(input("Enter a number : "))
result=value
if(value<0):
    result=value*(-1)
print("Input : ",value,"\tOutput : ",result)
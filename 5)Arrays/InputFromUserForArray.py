from array import *
val=array('i',[])
n=int(input("Enter number of elements to take : "))
for i in range(n):
    x=int(input("Enter a value : "))
    val.append(x) #We can use append() to insert an element to the array
#print(val)
item=int(input("Enter the value to serach : "))
for i in range(len(val)):
    if(val[i]==item):
        break
if(i==(len(val)-1) and val[i]!=item):
    print("Item Not Found")
else:
    print("Item found at : ",i)


#WHILE LOOP
#-------------

i=1
while(i<=5):
    print("Hello",i)
    i=i+1
print(i)
while(i>=0):
    print("Back",i)
    i=i-1

#Nested While
i=0
j=0
while(i<5):
    print("Cloud")
    j=0
    while(j<3):
        print("Onedrive")
        j=j+1
    i=i+1

# FOR LOOP: Used with sequence
# ----------

lst=['Rohit',25,69.3]
for i in lst:
    print(i)

str="Rohit Pandey"
for i in str:
    print(i)

for i in [10,20,30,40,50]:
    print(i)

for i in range(10):
    print(i)

for i in range(11,20):
    print(i)

for i in range(20,11,-1):
    print(i)

for i in range(0,20):
    if(i%5!=0):
        print(i)

# BREAK CONTINUE PASS

av=5
x=int(input("How many candy you want? : "))
i=1
while(i<=x):
    if(i>av):
        print("Sorry ! Out of stock")
        break       #the loop will be terminated here
    print("Take it")       
    i=i+1
print("BYE")

for i in range(1,101):
    if(i%3==0 and i%5==0):
        continue   # dont do anything below this statement in the loop,just go for next iteration
    print(i)
print("Bye")

for i in range(1,100):
    if(i%2==0):
        pass    #If i dont have anything to write for this block,i will use pass
    else:
        print(i)


#FOR_ELSE:
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for i in range(5):
    print("Hello")
else:
    print("Finally Finished")
    

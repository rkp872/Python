import math
count=0
num=int(input("Enter the number to test : "))
for i in range(2,int (math.sqrt(num))):
    if(num%i==0):
        count+=1
        break
if(count==0):
    print(num, " is a prime mumber")
else:
    print(num, " is not  a prime mumber")

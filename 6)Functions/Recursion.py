#--------------------------
#FACTORIAL
#----------------------

n=int(input("Enter a number : "))
def fact(n):
    if(n==1):
        return 1
    return(n*fact(n-1))
res=fact(n)
print("Fact of {} is {}".format(n,res))

#-------------------------------------
#FIBONACCI SERIES
#--------------------------------------

def fibo(n,f1,f2):
    if(n==1 or n==0):
        return
    print(f1,end=" ")
    fibo(n-1,f2,f1+f2)
print("Fibonacci series is : ",end=" ")
fibo(n,0,1)

#--------------------------------
#GCD 
#--------------------------------

def gcd(a,b): 
      
    # Everything divides 0  
    if (b == 0): 
         return a 
    return gcd(b, a%b) 
  
# Driver program to test above function 

a=int(input("Enter a number : "))
b=int(input("Enter another number : "))
if(gcd(a, b)): 
    print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
    print('not found') 







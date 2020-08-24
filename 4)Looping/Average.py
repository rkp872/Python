# Take 10 integers from keyboard using loop and print their average value on the screen.
sum=0
for i in range(10):
    x=int(input("Enter Number : "))
    sum=sum+x
print("Average of all the numbers is : ",sum/10)

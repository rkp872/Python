# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("Please enter your salary : "));
serviceYear=int(input("For how long you are working with us ? : "))
bonous=0
if(serviceYear>5):
    bonous=(5/100)*salary
print("Your net amount is : ",salary+bonous)


# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# Modify the above question to allow student to sit 
# if he/she has medical cause. Ask user if he/she has
#  medical cause or not ( 'Y' or 'N' ) and print accordingly.


held=int(input("How many class held? : "))
attended=int(input("How many class attended? : "))
percent=(attended/held)*100
allowed=False
if(percent>75):
    allowed=True
print("Percentage of class attended : ",percent)
if(allowed==True):
    print("Student is allowed to sit in exam ")
else:
    med=input("Do you have medical cause: (Y or N)? : ")[0]
    if(med=='Y'):
        print("Student is allowed to sit in exam ")
    else:
        print("Student is not allowed to sit in exam ")
    

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quan=int(input("Enter the number of items purchased : "))
total=quan*100;
discount=0;
if(total>1000):
    discount=(10/100)*total

print("Total amount to be paid : ",total-discount)
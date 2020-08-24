# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if 
# the year is century year like 2000, 1900, 2100 then 
# it must be divisible by 400.

year=int(input("Enter year to check :"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap Year")
        else:
            print("Non Leap Year")
    else:
        print("Leap Year")
else:
    print("Non Leap Year")
    
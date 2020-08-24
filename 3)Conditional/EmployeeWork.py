# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR".

age=int(input("Enter Your age : "))
sex=input("Your sex (M or F)? : ")
if(sex=='F'):
    print("You should work in Urban areas")
else:
    if(age>=20 and age<40):
        print("You can work anywhere")
    elif(age>=40 and age<60):
        print("You should work in urban areas only")
    else:
        print("ERROR")
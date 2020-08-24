
# Take input of age of 3 people by user and determine oldest and youngest among them.
user1=int(input("Hi! user1 Please Enter Your Age : "))
user2=int(input("Hi! user2 Please Enter Your Age : "))
user3=int(input("Hi! user3 Please Enter Your Age : "))

if(user1<user2 and user1<user3):
    print("User1 is youngest ")
elif(user2<user1 and user2<user3):
    print("User2 is Youngest")
elif(user3<user1 and user3<user2):
    print("User3 is Youngest")
else:
    print("Invalid age")
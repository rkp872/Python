
# In Python, exceptions can be handled using a try statement.

# The critical operation which can raise an exception is placed inside
# the try clause. The code that handles the exceptions is written
# in the except clause.


#  The try statement in Python can have an optional finally clause. 
#  This clause is executed no matter what, and is generally used 
#  to release external resources.
a=5
b=6
try:
    print("Resource opened")
    print(a/b)
    k=int(input("Enter a number : "))
    print(k)
except ZeroDivisionError:   
    print("Division by Zero : ")

except ValueError:
    print("Invalid input ")

except Exception as e:
    print("ERROR : ", e)

finally:
    print("Resource closed")

print("Hello")


#  We can also manually raise exceptions using the raise keyword.
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)

   
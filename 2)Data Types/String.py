# String    :String are the element which is enclosed within '' or "" .

st="rohit Pandey"
print(type(st))
st2='Ananya Adhikary'
print(st)
print(st2)

print(len(st))
print(st.capitalize())  #Capitalize the first letter of the string

print(st.index('P'))
print(st.isalnum())
print(st.isalpha())
print(st.isascii())
print(st.isnumeric())

num="14587"
print(num.isnumeric())

al='D'  #In python we have nothing called char..
        # Single charecter is also considered as string only
print(al.islower())
print(al.isupper())

al2='d'
print(al2.islower())
print(al2.isupper())
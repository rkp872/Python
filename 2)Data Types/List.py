# List  : List are the growable collection of hetrogeneous elements enclosed within []

lst=[10,20,30,40,50,60]
print(lst)
print(type(lst))

print(lst[0])   #Accessing list by index.  Positive index: [0,1,2,3,4...]
print(lst[1:3]) # Slicing list
print(lst[2:])
print(lst[:3])
print(lst[-1])  #Negative index will traverse list from backward . Negative index:   [., . , ., -3,-2,-1]

lst.append(70)  #Adding single element in last
print(lst)

lst2=lst.copy()
print(lst2)

print(lst.count(10))    #count Frequency of 10 in list

lst.extend([70,80,90])  # Adding multiple elemnts in last
print(lst)

print(lst.index(70))

lst.insert(3,25)    # Insert 25 at index 3
print(lst)

print(lst.pop()) #removes and return lst element of the list

lst.remove(25) # Removes 25 from list

print(lst)  

lst.reverse()   # reverses the list
print(lst)

lst.sort()  #sort the list
print(lst)

print(len(lst))
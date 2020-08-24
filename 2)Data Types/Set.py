# Set:  Set are the collection of hetrogeneous elements enclosed within {}
    #   Sets does not allows duplicates and insertion order is not preserved
    #Elements are inserted according to the order of their hash value

set1={10,20,20,30,50,40,60}
print(set1)
print(type(set1))

set1.add(36)
print(set1)

set2=set1.copy()
print(set2)

set2.remove(20)
set2.remove(60)
print(set2)

print(set1.difference(set2))  #returns elements which are present in set1 but not in set2  

print(set2.difference(set1))  #returns elements which are present in set2 but not in set1

print(set1.intersection(set2))  #Returns intersection of two sets

print(set1.union(set2)) #Returns Union of two sets
print(len(set1))
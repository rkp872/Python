myList=[]
n=int(input("Enter number of elements in the list: "))
for i in range(n):
    tem=int(input("Enter a value: "))
    myList.append(tem)
def evenOdd(list):
    even=0
    odd=0
    for i in list:
        if(i%2==0):
            even=even+1
        else:
            odd=odd+1
    return even,odd
even,odd=evenOdd(myList)
# print("Number of even: ",even)
# print("Print Number of odd: ",odd)
print("Even : {} and Odd : {}".format(even,odd))    #format() replaces the {} 
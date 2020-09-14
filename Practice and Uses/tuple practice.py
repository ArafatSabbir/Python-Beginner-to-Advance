myTuple = (1,2,3,[10,20,30])       # assign tuple
myTuple[3][2] = 31                 # change elemet inside tuple object
print (myTuple)
print("--------------------------------------------------------------------------" )

myTuple2 = (7,8,9)
mergedTuple = myTuple + myTuple2   # join 2 tuple
print(mergedTuple)
print("--------------------------------------------------------------------------" )

myTuple3 = (1,1,2,2,2,2,3,3,3)
print (myTuple3.count(2))          # count return number of count of an element.
print("--------------------------------------------------------------------------" )

myList = [5,6,7]
newTuple1 = tuple(myList)          # convert list to tuple
print(newTuple1)
print("--------------------------------------------------------------------------" )


for i in newTuple1:                # itteration
    print(i)

print("--------------------------------------------------------------------------" )

print (5 in newTuple1 )            # mebership check in tuple
print (8 in newTuple1 )
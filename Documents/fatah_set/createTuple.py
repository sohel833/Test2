# 1. Write a Python program to create a tuple.
mytupleList=[]
length = int(input("enter the length of the tuple: "))
for x in range(length):
    elements = input("enter the elements of the tuple")
    mytupleList.append(elements)
mytupleList = tuple(mytupleList)
print("Tuple : ",mytupleList)
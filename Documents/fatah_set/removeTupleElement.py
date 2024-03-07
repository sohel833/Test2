# 8. Write a Python program to remove an item from a tuple.
mytupleList = []
length = int(input("enter the length of the tuple: "))
for x in range(length):
    elements = input(f"enter the elements of the tuple at {x + 1} position : ")
    if elements.isdigit():
        mytupleList.append(int(elements))
        # print(elements)
    elif "." in elements:
        mytupleList.append(float(elements))
        # print(elements)
    elif ('True' or 'False') in elements:
        mytupleList.append(bool(elements))
        # print(elements)
    else:
        mytupleList.append(elements.strip())
        # print(elements)
mytuple = tuple(mytupleList)
print(f"Tuple : ", mytuple)
removeElements = input("Enter the element to remove from the above tuple : ")
for x in mytupleList:
    if removeElements in mytupleList:
        if removeElements.isdigit():
            mytupleList.remove(int(removeElements))
            # print(elements)
        elif "." in removeElements:
            mytupleList.remove(float(removeElements))
            # print(elements)
        elif ('True' or 'False') in removeElements:
            mytupleList.remove(bool(removeElements))
            # print(elements)
        else:
            mytupleList.remove(removeElements.strip())

print("Tuple after removing the element: ",tuple(mytupleList))
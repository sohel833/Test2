# 2. Write a Python program to create a tuple with different data types.
mytupleList=[]
length = int(input("enter the length of the tuple: "))
for x in range(length):
    elements = input("enter the elements of the tuple")
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
mytupleList = tuple(mytupleList)
print("Tuple : ",mytupleList)
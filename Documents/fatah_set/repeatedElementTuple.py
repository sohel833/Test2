# 5. Write a Python program to find the repeated items of a tuple.
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
repeatedElementsTuple = []
for x in mytupleList:
    if x in mytupleList:
        c = mytupleList.count(x)
    if c > 1:
        repeatedElementsTuple.append(x)
repeatedElementsTuple = set(repeatedElementsTuple)
repeatedElementsTuple = tuple(repeatedElementsTuple)
print("Given Tuple : ",tuple(mytupleList))
print("Repeated Elements Tuple : ", repeatedElementsTuple)
mytuple = tuple(mytupleList)
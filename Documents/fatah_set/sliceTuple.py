# 9. Write a Python program to slice a tuple.
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
startIndex = int(input("Enter the number of position from where you want to start : "))
endIndex = int(input("Enter the number of position  where you want to stop : "))
# print(mytuple[startIndex:endIndex])
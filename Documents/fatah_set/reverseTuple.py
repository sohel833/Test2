# 10. Write a Python program to reverse a tuple.
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
enteredTuple = tuple(mytupleList)
mytupleList.reverse()
mytuple = tuple(mytupleList)
print(f"Entered tuple : {enteredTuple}\nReversed Tuple : {mytuple}")
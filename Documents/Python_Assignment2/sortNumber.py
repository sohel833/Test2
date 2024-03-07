# print("########################################### SORT NUMBER START##################################################")
# # 5. Write a Python program to get a list, sorted in increasing order by the last
# # element in each tuple from a given list of non-empty tuples. Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# # Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
unsorted_list = []
length_of_unsorted_list = int(input("Enter the length of the list: "))
for x in range(length_of_unsorted_list):
    element_input = input(
        '''Enter tuple element here by comma seperated when you want to move to the next entry of tuple do not give "
comma just hit the enter : ''')
    elements = element_input.split(",")
    print(type(elements))
    print(elements)
# size = len(elements[0])
# for x in range(len(elements)):
#     if x == size:
    converted_list = []
    for element in elements:
        if element.isdigit():
            converted_list.append(int(element))
        elif "." in element:
            converted_list.append(float(element))
        else:
            converted_list.append(element.strip())
    unsorted_list.append(tuple(converted_list))
length = len(unsorted_list[0])
unsorted_list.sort(key=lambda x: x[0], reverse=False)
print("Here is your sorted list based on the last element of tuple in decreasing manner = ", unsorted_list)

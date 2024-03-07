# List
from itertools import permutations

print("########################################### SUM NUMBER START###################################################")
# 1. Write a Python program to sum all the items in a list.
# sum_list = []
# length_of_list = int(input("Enter the length of the list: "))
# for x in range(length_of_list):
#     element=int(input(f"enter thr {x+1} th element "))
#     sum_list.append(element)
# print(f"sum of the list = ",sum(sum_list))
print("########################################### MULTIPLY NUMBER START##############################################")
# 2. Write a Python program to multiplies all the items in a list.
# mul_list = []
# length_of_list = int(input("Enter the length of the list: "))
# mul_values = 1
# for x in range(length_of_list):
#     element=int(input(f"enter thr {x+1} th element "))
#     mul_list.append(element)
#     mul_values = mul_values * mul_list[x]
# print(f"multiplication of the lis = ", mul_values)
print("########################################### SMALLEST NUMBER START##############################################")
# 3. Write a Python program to get the smallest number from a list.
# small_list = []
# length_of_list = int(input("Enter the length of the list: "))
# for x in range(length_of_list):
#     element=int(input(f"enter thr {x+1} th element "))
#     small_list.append(element)
# minimum=small_list[0]
# for x in small_list:
#     if x < minimum:
#         minimum = x
# print(f"smallest number of the list = ",minimum)
print("########################################### COUNT NUMBER START#################################################")
# 4. Write a Python program to count the number of strings where the string length
# is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# count = 0
# sample_list = []
# length_of_list = (int(input("Enter the length of the list: ")))
# for x in range(length_of_list):
#     element = (input(f"Enter the element at {x+1} of the list: "))
#     sample_list.append(element)
# print(sample_list)
# for x in sample_list:
#     if len(x) > 2:
#         length = len(x)
#         if x[0] == x[length - 1]:
#             count += 1
# print(count)
print("########################################### SORT NUMBER START##################################################")
# 5. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples. Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# unsorted_list = []
# length_of_unsorted_list = int(input("Enter the length of the list: "))
# for x in range(length_of_unsorted_list):
#     element_input = input(
#         '''Enter tuple element here by comma seperated when you want to move to the next entry of tuple do not give "
# comma just hit the enter : ''')
#     elements = element_input.split(",")
#     print(type(elements))
#     print(elements)
# # size = len(elements[0])
# # for x in range(len(elements)):
# #     if x == size:
#     converted_list = []
#     for element in elements:
#         if element.isdigit():
#             converted_list.append(int(element))
#         elif "." in element:
#             converted_list.append(float(element))
#         else:
#             converted_list.append(element.strip())
#     unsorted_list.append(tuple(converted_list))
# length = len(unsorted_list[0])
# unsorted_list.sort(key=lambda x: x[0], reverse=False)
# print("Here is your sorted list based on the last element of tuple in decreasing manner = ", unsorted_list)
print("########################################### DUPLICATE NUMBER START#############################################")
# 6. Write a Python program to remove duplicates from a list.
# common_list = []
# length_of_common_list = int(input("Enter the length of the list: "))
# for x in range(length_of_common_list):
#     element = input(f"Enter the element at {x + 1} position = ")
#     common_list.append(element)
#     original_list = common_list
#     for i in range(len(common_list)):
#         for j in range(i + 1, len(common_list)):
#             if common_list[i] == common_list[j]:
#                 common_list.remove(common_list[j])
# print("The list after removing duplicates = ", common_list)
print("########################################### COPYING LIST START#################################################")
# 7. Write a Python program to clone or copy a list.
# listC = []
# length_of_common_list = int(input("Enter the length of the list: "))
# for x in range(length_of_common_list):
#     element = input(f"Enter the element at {x + 1} position = ")
#     listC.append(element)
# list_copy=listC.copy()
# print("Copy of the listC = ",list_copy)
print("########################################### ELEMENT LARGER THAN LENGTH OF THE LIST START#######################")
# 8. Write a Python program to find the list of words that are longer than n froma
# given list of words.
# list_words = []
# expected_list = []
# length_of_common_list = int(input("Enter the length of the list: "))
# for x in range(length_of_common_list):
#     element = input(f"Enter the element at {x + 1} position = ")
#     list_words.append(element)
# for x in range(len(list_words)):
#     if len(list_words[x])>len(list_words):
#         print((list_words[x]))
print("########################################### COMMON LIST START##################################################")
# 9. Write a Python function that takes two lists and returns True if they have at
# least one common member.
# first_list = []
# second_list = []
# isPresent = False
# length_of_common_Flist = int(input("Enter the length of the list: "))
# for x in range(length_of_common_Flist):
#     element = input(f"Enter the element at {x + 1} position = ")
#     first_list.append(element)
# length_of_common_Slist = int(input("Enter the length of the list: "))
# for x in range(length_of_common_Slist):
#     element = input(f"Enter the element at {x + 1} position = ")
#     second_list.append(element)
# for x in range(len(first_list)):
#     for y in range(len(second_list)):
#         if first_list[x] == second_list[y]:
#             isPresent = True
# if isPresent:
#     print(isPresent," :Yes there is match")
# else:
#     print(isPresent," : No there is no match")
print("########################################### REMOVING SPECIFIC LIST ELEMENT START###############################")
# 10. Write a Python program to print a specified list after removing the 0th, 4th and
# 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
# isPresent = False
# listR = []
# length_of_common_Flist = int(input("Enter the length of the list: "))
# for x in range(length_of_common_Flist):
#     element = input(f"Enter the element at {x + 1} position = ")
#     listR.append(element)
# if length_of_common_Flist >= 6:
#     listR.remove(listR[0])
#     listR.remove(listR[3])
#     listR.remove(listR[3])
#     print(listR)
# else:
#     print("Please enter the length of the list more than or equal to 6 ")
print("########################################### PERMUTATION LIST START##################################################")
# 11. Write a Python program to generate all permutations of a list in Python.
# listP = []
# length_of_common_Flist = int(input("Enter the length of the list: "))
# for x in range(length_of_common_Flist):
#     element = input(f"Enter the element at {x + 1} position = ")
#     listP.append(element)
# perms = permutations(listP)
# for perm in perms:
#     print("Permutations of list = ",perm)
print("########################################### DIFF BTWN LIST START###############################################")
# 12. Write a Python program to get the difference between the two lists.
# first_list = []
# second_list = []
# difference_list = []
# isPresent = False
# length_of_common_Flist = int(input("Enter the length of the list: "))
# for x in range(length_of_common_Flist):
#     element = input(f"Enter the element at {x + 1} position = ")
#     first_list.append(element)
# length_of_common_Slist = int(input("Enter the length of the list: "))
# for x in range(length_of_common_Slist):
#     element = input(f"Enter the element at {x + 1} position = ")
#     second_list.append(element)
# for i in first_list:
#     if i not in second_list:
#         difference_list.append(i)
# for j in second_list:
#     if j not in first_list:
#         difference_list.append(j)
# print("The difference between two list = ",difference_list)
print("########################################### APPEND LIST START##################################################")
# 13. Write a Python program to append a list to the second list.
# 14. Write a python program to check whether two
# lists are circularly identical.
# 15. Write a Python program to find common items from two lists.
first_list = []
second_list = []
difference_list = []
isPresent = False
length_of_common_Flist = int(input("Enter the length of the list: "))
for x in range(length_of_common_Flist):
    element = input(f"Enter the element at {x + 1} position = ")
    first_list.append(element)
length_of_common_Slist = int(input("Enter the length of the list: "))
for x in range(length_of_common_Slist):
    element = input(f"Enter the element at {x + 1} position = ")
    second_list.append(element)
for i in first_list:
    if i  in second_list:
        difference_list.append(i)
# for j in second_list:
#     if j  in first_list:
#         difference_list.append(j)
print("The difference between two list = ",difference_list)
# 16. Write a Python
# program to split a list based on first character of word.
# 17. Write a Python program to remove duplicates from a
# list of lists. Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] New List : [[10, 20], [30, 56,
# 25], [33], lis = [1,2,3] for x in range(len(lis)): for y in range(x+1,len(lis)): print(lis[x],lis[y])

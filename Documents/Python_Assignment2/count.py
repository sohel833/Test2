print("########################################### COUNT NUMBER START#################################################")
# 4. Write a Python program to count the number of strings where the string length
# is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
count = 0
sample_list = []
length_of_list = (int(input("Enter the length of the list: ")))
for x in range(length_of_list):
    element = (input(f"Enter the element at {x+1} of the list: "))
    sample_list.append(element)
print(sample_list)
for x in sample_list:
    if len(x) > 2:
        length = len(x)
        if x[0] == x[length - 1]:
            count += 1
print(count)
print("########################################### SUM NUMBER START###################################################")
# 1. Write a Python program to sum all the items in a list.
sum_list = []
length_of_list = int(input("Enter the length of the list: "))
for x in range(length_of_list):
    element=int(input(f"enter thr {x+1} th element "))
    sum_list.append(element)
print(f"sum of the list = ",sum(sum_list))
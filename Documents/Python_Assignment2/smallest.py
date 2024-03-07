print("########################################### SMALLEST NUMBER START##############################################")
# 3. Write a Python program to get the smallest number from a list.
small_list = []
length_of_list = int(input("Enter the length of the list: "))
for x in range(length_of_list):
    element=int(input(f"enter thr {x+1} th element "))
    small_list.append(element)
minimum=small_list[0]
for x in small_list:
    if x < minimum:
        minimum = x
print(f"smallest number of the list = ",minimum)
print("########################################### MULTIPLY NUMBER START##############################################")
# 2. Write a Python program to multiplies all the items in a list.
mul_list = []
length_of_list = int(input("Enter the length of the list: "))
mul_values = 1
for x in range(length_of_list):
    element=int(input(f"enter thr {x+1} th element "))
    mul_list.append(element)
    mul_values = mul_values * mul_list[x]
print(f"multiplication of the lis = ", mul_values)
#4 * 3 * 2 * 1 = 1 * 2 * 3 * 4

number = int(input("Enter the number to now the factorial: "))
if number>0:
    factorial = 1
    for x in range(1,number+1):
        factorial = factorial * x  # 1 * 1 * 1,
print(f"factorial = {factorial}")
power_of_two = '''
# 4. Power of 2
# a. Desc -> This program takes a command-line argument N and prints a table of the
# powers of 2 that are less than or equal to 2^N.
# b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
# c. Logic -> repeat until i equals N.
'''
number = int(input("Enter the number: "))
if 0 <= number <= 33:
    for i in range(number + 1):
        powerOf2 = 2 ** i
        print(f"2 ^ {i}   =   {powerOf2}")
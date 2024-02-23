# 1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
# a. I/P -> Take Username as Input. Ensure UserName has min 3 char
# b. Logic -> Replace <<UserName>> with the proper name
# c. O/P -> Print the String with username
#
# username = input("Enter Your Name: ")
# Greetings = "Hello <<UserName>>, How are you?"
# GreetingsOutput = Greetings.replace("<<UserName>>",username)
# print(GreetingsOutput)
# import random
###########################################

# 2. Flip Coin and print percentage of Heads and Tails
# a. I/P -> The number of times to Flip Coin. Ensure it is positive integer. b. Logic ->
# Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
# c. O/P -> Percentage of Head vs Tails


# no_of_flips = int(input("Enter Your Name: "))
# #ensuring positive number
# if no_of_flips > 0:
#     count_head = 0
#     count_tails = 0
# #itterating the no of flips
#     for x in range(no_of_flips):
# #randomly select the values between o and 1
#         random_number =random.randint(0,1)
# #if no of random_number occurrences are < 0.5 counts tails as 1
#         if random_number < 0.5:
#             count_tails += 1
# #if no of random_number occurrences are => 0.5 counts heads as 1
#         else:
#             count_head +=1
# #percentage on number of random_number occurrences with condition mentioned above
#     percentage_of_heads = (count_head/no_of_flips)*100
#     percentage_of_tails = 100-percentage_of_heads
#
#     print(f"The percentage of heads: {percentage_of_heads}")
#     print(f"The percentage of tails: {percentage_of_tails}")
# else:
#     print("Please Enter the correct Value")

###############################################################################################################

# 3. Leap Year
# a. I/P -> Year, ensure it is a 4-digit number.
# Year = int(input("Enter year in 4 digits to know leap year or not: "))
# # b. Logic -> Determine if it is a Leap Year.
# if 1000<= Year <=9999:
#
#     if (Year%4==0  and Year%100!=0) or Year%400==0:
#         print(f"The year {Year} is a leap year")
#     else:
#         print(f"The year {Year} is a not a leap year")
# else:
#     print("Please enter the year in 4 digits only")

###############################################################################################################

# 4. Power of 2
# a. Desc -> This program takes a command-line argument N and prints a table of the
# powers of 2 that are less than or equal to 2^N.
# b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
# c. Logic -> repeat until i equals N.
# number = int(input("Enter the number: "))
# if 0 <= number <= 33:
#     for i in range(number + 1):
#         powerOf2 = 2 ** i
#         print(f"2 ^ {i}   =   {powerOf2}")


###############################################################################################################

# 5. Harmonic Number
# a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
# number = int(input("Please enter the number: "))
# harmonic_number = 0
# for i in range(1,number+1):
#     harmonic_number = harmonic_number+1/i #0+1,1+1/2,1+1/2+1/3....
# print(float(harmonic_number))
    # if i == number:
    #     break




# (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
# b. I/P -> The Harmonic Value N. Ensure N != 0
# c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
# d. O/P -> Print the Nth Harmonic Value.


# 6. Factors
# a. Desc -> Computes the prime factorization of N using brute force.
# b. I/P -> Number to find the prime factors
# c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
# d. O/P -> Print the prime factors of number N.


#4 * 3 * 2 * 1 = 1 * 2 * 3 * 4
number = int(input("Enter the number to now the factor: "))
if number>0:
    factorial = 1
    for x in range(1,number+1):
        factorial = factorial * x  # 1 * 1 * 1,
print(f"factorial = {factorial}")
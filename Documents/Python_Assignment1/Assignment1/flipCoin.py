import random

'''
2. Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer. b. Logic ->
Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
c. O/P -> Percentage of Head vs Tails
'''
no_of_flips = int(input("Enter the Flips: "))
# ensuring positive number
if no_of_flips > 0:
    count_head = 0
    count_tails = 0
    # itterating the no of flips
    for x in range(no_of_flips):
        # randomly select the values between o and 1
        random_number = random.randint(0, 1)
        # if no of random_number occurrences are < 0.5 counts tails as 1
        if random_number < 0.5:
            count_tails += 1
        # if no of random_number occurrences are => 0.5 counts heads as 1
        else:
            count_head += 1
    # percentage on number of random_number occurrences with condition mentioned above
    percentage_of_heads = (count_head / no_of_flips) * 100
    percentage_of_tails = 100 - percentage_of_heads

    print(f"The percentage of heads: {percentage_of_heads}")
    print(f"The percentage of tails: {percentage_of_tails}")
else:
    print("Please Enter the correct Value")

# 3. Leap Year
# a. I/P -> Year, ensure it is a 4-digit number.
Year = int(input("Enter year in 4 digits to know leap year or not: "))
# b. Logic -> Determine if it is a Leap Year.
if 1000 <= Year <= 9999:

    if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
        print(f"The year {Year} is a leap year")
    else:
        print(f"The year {Year} is a not a leap year")
else:
    print("Please enter the year in 4 digits only")

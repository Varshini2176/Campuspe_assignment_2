try:
    year = int(input("Enter a year: "))

    if year % 4 == 0:
        if year % 100 != 0:
            print(f"{year} is a LEAP year.")
            print("Reason: Divisible by 4 and not divisible by 100.")
        elif year % 400 == 0:
            print(f"{year} is a LEAP year.")
            print("Reason: Divisible by 400.")
        else:
            print(f"{year} is NOT a leap year.")
            print("Reason: Divisible by 100 but not divisible by 400.")
    else:
        print(f"{year} is NOT a leap year.")
        print("Reason: Not divisible by 4.")

except ValueError:
    print("Invalid input! Please enter a valid year.")
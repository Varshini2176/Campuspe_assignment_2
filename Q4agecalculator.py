try:
    
    birth_year = int(input("Enter your birth year: "))

   
    current_year = 2026
    age = current_year - birth_year
    months = age * 12
    days = age * 365   # Approximation
    hours = days * 24
    minutes = hours * 60
    years_to_100 = 100 - age

    print("\n AGE DETAILS ")
    print("Current Age:", age, "years")
    print("Age in Months:", months)
    print("Age in Days (approx):", days)
    print("Age in Hours:", hours)
    print("Age in Minutes:", minutes)

    if years_to_100 > 0:
        print("Years until 100:", years_to_100)
    else:
        print("You are already 100 or older!")

except ValueError:
    print("Invalid input! Please enter a valid year.")

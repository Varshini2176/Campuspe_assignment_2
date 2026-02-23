try:
    b_day = int(input("Enter your birth day (1-31): "))
    b_month = int(input("Enter your birth month (1-12): "))
    b_year = int(input("Enter your birth year: "))

    c_day = int(input("Enter current day: "))
    c_month = int(input("Enter current month: "))
    c_year = int(input("Enter current year: "))

    age_years = c_year - b_year

    if (c_month, c_day) < (b_month, b_day):
        age_years -= 1

    total_days = (c_year - b_year) * 365 + (c_month - b_month) * 30 + (c_day - b_day)

    total_hours = total_days * 24
    total_minutes = total_hours * 60
    total_months = age_years * 12
    years_to_100 = 100 - age_years

    print("\nEXACT AGE DETAILS")
    print("Current Age:", age_years, "years")
    print("Age in Months:", total_months)
    print("Age in Days (approx):", total_days)
    print("Age in Hours:", total_hours)
    print("Age in Minutes:", total_minutes)

    if years_to_100 > 0:
        print("Years until 100:", years_to_100)
    else:
        print("You are already 100 or older!")

except ValueError:
    print("Invalid date entered! Please check your inputs.")
try:
    age = int(input("Enter age: "))
    day = input("Enter day of the week: ").strip().lower()
    tickets = int(input("Enter number of tickets: "))

    if tickets <= 0:
        print("Number of tickets must be greater than 0.")
    else:
        if age < 3:
            price = 0
            category = "Free"
        elif 3 <= age <= 12:
            price = 150
            category = "Child"
        elif 13 <= age <= 59:
            price = 300
            category = "Adult"
        else:
            price = 200
            category = "Senior"

        base_total = price * tickets
        if day in ["friday", "saturday", "sunday"]:
            discount = 0.20 * base_total
        elif day in ["monday", "tuesday", "wednesday", "thursday"]:
            discount = 0
        else:
            print("Invalid day entered.")
            exit()

        final_amount = base_total - discount

        #results
        print("\nTICKET BILL")
        print("Category:", category)
        print("Base price per ticket: ₹", price)
        print("Total before discount: ₹", base_total)
        print("Discount: ₹", round(discount, 2))
        print("Final Amount: ₹", round(final_amount, 2))

except ValueError:
    print("Invalid input! Please enter valid numbers.")
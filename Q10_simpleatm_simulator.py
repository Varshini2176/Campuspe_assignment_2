balance = 10000

while True:
    print("\nsimple atm simulator")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print(f"Current Balance: {balance}")

        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print(f"Updated Balance: {balance}")
            else:
                print("Deposit amount must be positive.")

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("Insufficient balance!")
            elif balance - amount < 500:
                print("Minimum balance of 500 must be maintained.")
            else:
                balance -= amount
                print("Withdrawal successful!")
                print(f"Updated Balance: {balance}")

        elif choice == 4:
            print("Thank you for using ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 4.")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


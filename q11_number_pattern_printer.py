# Q11: Number Pattern Printer

def pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern2(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

def pattern3(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def pattern4(n):
    for i in range(1, n + 1):
        # Ascending
        for j in range(1, i + 1):
            print(j, end="")
        # Descending
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

while True:
    print("\n===== NUMBER PATTERN PRINTER =====")
    print("1. Pattern 1")
    print("2. Pattern 2")
    print("3. Pattern 3")
    print("4. Pattern 4")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting program.")
            break

        height = int(input("Enter height: "))

        if height <= 0:
            print("Height must be positive.")
        else:
            print("\nGenerated Pattern:\n")

            if choice == 1:
                pattern1(height)
            elif choice == 2:
                pattern2(height)
            elif choice == 3:
                pattern3(height)
            elif choice == 4:
                pattern4(height)
            else:
                print("Invalid choice!")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
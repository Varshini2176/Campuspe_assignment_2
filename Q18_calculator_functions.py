def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero not allowed."
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot find square root of negative number."
    return a ** 0.5

def percentage(a, b):
    if b == 0:
        return "Error: Cannot calculate percentage with zero."
    return (a / b) * 100

def calculator():
    while True:
        print("\n ADVANCED CALCULATOR")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. Percentage")
        print("9. Exit")

        try:
            choice = int(input("Enter your choice (1-9): "))

            if choice == 9:
                print("Exiting calculator. Goodbye!")
                break

            if choice in [1, 2, 3, 4, 5, 6]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    print("Result:", add(a, b))
                elif choice == 2:
                    print("Result:", subtract(a, b))
                elif choice == 3:
                    print("Result:", multiply(a, b))
                elif choice == 4:
                    print("Result:", divide(a, b))
                elif choice == 5:
                    print("Result:", modulus(a, b))
                elif choice == 6:
                    print("Result:", power(a, b))

            elif choice == 7:
                a = float(input("Enter number: "))
                print("Result:", square_root(a))

            elif choice == 8:
                a = float(input("Enter value: "))
                b = float(input("Enter total value: "))
                print("Result:", percentage(a, b), "%")

            else:
                print("Invalid choice! Please select between 1 and 9.")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

calculator()

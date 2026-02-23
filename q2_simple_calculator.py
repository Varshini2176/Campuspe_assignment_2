try:
    n1= float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    print("\nResults:")

    # Addition
    print(f"{n1} + {n2} = {n1 + n2}")

    # Subtraction
    print(f"{n1} - {n2} = {n1 - n2}")

    # Multiplication
    print(f"{n1} * {n2} = {n1 * n2}")

    # Division
    if n2 != 0:
        print(f"{n1} / {n2} = {round(n1 / n2, 2)}")
    else:
        print("Division by zero is not allowed.")

    # Modulus
    if n2 != 0:
        print(f"{n1} % {n2} = {n1 % n2}")
    else:
        print("Modulus by zero is not allowed.")

    # Exponentiation
    print(f"{n1} ^ {n2} = {n1 ** n2}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
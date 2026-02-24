try:
    n1= float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    print("\nResults:")

    # Addition
    print(f"{no1} + {n02} = {no1 + no2}")

    # Subtraction
    print(f"{no1} - {no2} = {no1 - no2}")

    # Multiplication
    print(f"{no1} * {no2} = {no1 * no2}")

    # Division
    if no2 != 0:
        print(f"{no1} / {no2} = {round(no1 / no2, 2)}")
    else:
        print("Division by zero is not allowed.")

    # Modulus
    if no2 != 0:
        print(f"{no1} % {no2} = {no1 % no2}")
    else:
        print("Modulus by zero is not allowed.")

    # Exponentiation
    print(f"{no1} ^ {no2} = {no1 ** no2}")

except ValueError:

    print("Invalid input! Please enter numeric values only.")

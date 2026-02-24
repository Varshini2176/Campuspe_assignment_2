def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def sum_of_digits(n):
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total

def reverse_number(n):
    return int(str(n)[::-1])

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** power
    return total == n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    if n <= 1:
        return False
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

def math_menu():
    while True:
        print("\nNUMBER SYSTEM MENU")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        try:
            choice = int(input("Enter choice (1-10): "))

            if choice == 10:
                print("Exiting program.")
                break

            elif choice == 1:
                n = int(input("Enter number: "))
                print("Factorial:", factorial(n))

            elif choice == 2:
                n = int(input("Enter number: "))
                print("Prime:" if is_prime(n) else "Not Prime")

            elif choice == 3:
                n = int(input("Enter position: "))
                print("Fibonacci number:", fibonacci(n))

            elif choice == 4:
                n = int(input("Enter number: "))
                print("Sum of digits:", sum_of_digits(n))

            elif choice == 5:
                n = int(input("Enter number: "))
                print("Reversed number:", reverse_number(n))

            elif choice == 6:
                n = int(input("Enter number: "))
                print("Armstrong:" if is_armstrong(n) else "Not Armstrong")

            elif choice == 7:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == 8:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == 9:
                n = int(input("Enter number: "))
                print("Perfect Number:" if is_perfect_number(n) else "Not Perfect")

            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter integers only.")

math_menu()

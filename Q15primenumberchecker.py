try:
    num = int(input("Enter a number: "))

    if num <= 1:
        print(f"{num} is NOT a prime number.")
    elif num == 2:
        print("2 is a PRIME number.")
    else:
        is_prime = True
        i = 2

        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            print(f"{num} is a PRIME number.")
        else:
            print(f"{num} is NOT a prime number.")

    # Part 2: Prime Numbers in Range
    start = int(input("\nEnter start range: "))
    end = int(input("Enter end range: "))

    print(f"\nPrime numbers between {start} and {end}:")

    for number in range(start, end + 1):
        if number > 1:
            prime_flag = True
            i = 2
            while i * i <= number:
                if number % i == 0:
                    prime_flag = False
                    break
                i += 1
            if prime_flag:
                print(number, end=" ")

except ValueError:

    print("Invalid input! Please enter integers only.")

try:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    
    elif num == 0:
        print("0! = 1")
    
    else:
        factorial = 1
        expression = ""

        for i in range(num, 0, -1):
            factorial *= i
            expression += str(i)
            if i != 1:
                expression += " X "

        print(f"{num}! = {expression} = {factorial}")

except ValueError:
    print("Invalid input! Please enter an integer.")

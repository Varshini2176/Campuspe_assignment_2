# Q12: Multiplication Table Generator

try:
    number = int(input("Enter number: "))
    end_range = int(input("Enter range (end): "))

    if end_range <= 0:
        print("Range must be positive.")
    else:
        print(f"\nMultiplication Table of {number}\n")
        for i in range(1, end_range + 1):
            print(f"{number} x {i} = {number * i}")

except ValueError:
    print("Invalid input! Please enter integers only.")

# BONUS: Full Multiplication Table (1–10 Grid)

print("\nFull Multiplication Table (1–10)\n")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()
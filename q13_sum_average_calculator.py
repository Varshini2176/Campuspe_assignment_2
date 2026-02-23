try:
    count = int(input("How many numbers? "))

    if count <= 0:
        print("Count must be greater than 0.")
    else:
        numbers = []

        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            numbers.append(num)

        # Basic Calculations
        total = sum(numbers)
        average = total / count
        maximum = max(numbers)
        minimum = min(numbers)

        # Median Calculation
        numbers.sort()
        if count % 2 == 0:
            median = (numbers[count//2 - 1] + numbers[count//2]) / 2
        else:
            median = numbers[count//2]

        # Mode Calculation
        frequency = {}
        for num in numbers:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        max_freq = max(frequency.values())
        modes = []

        for key, value in frequency.items():
            if value == max_freq and max_freq > 1:
                modes.append(key)

        print("\n===== STATISTICAL RESULTS =====")
        print("Sum:", total)
        print("Average:", round(average, 2))
        print("Maximum:", maximum)
        print("Minimum:", minimum)
        print("Median:", median)

        if modes:
            print("Mode:", modes)
        else:
            print("Mode: No mode (all values occur once)")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
try:
    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for Subject {i}: "))
        
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100.")
            exit()
        marks.append(mark)
    total = sum(marks)
    percentage = total / 5
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"

    if all(mark >= 40 for mark in marks):
        result = "Pass"
    else:
        result = "Fail"

    # Results
    print("\nRESULT")
    for i in range(5):
        print(f"Subject {i+1}: {marks[i]}")
    print("Total Marks:", total, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
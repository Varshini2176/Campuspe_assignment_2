import random
best_score = None
while True:
    print("\n NUMBER GUESSING GAME")
    print("Select Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-1000)")

    try:
        difficulty = int(input("Enter choice (1-3): "))

        if difficulty == 1:
            lower, upper = 1, 50
            hint_range = 5
        elif difficulty == 2:
            lower, upper = 1, 100
            hint_range = 5
        elif difficulty == 3:
            lower, upper = 1, 1000
            hint_range = 10
        else:
            print("Invalid choice! Defaulting to Medium.")
            lower, upper = 1, 100
            hint_range = 5

        secret_number = random.randint(lower, upper)
        attempts = 7
        used_attempts = 0

        print(f"\n Guess a number between {lower} and {upper}")
        print("You have 7 attempts.\n")

        while attempts > 0:
            guess = int(input("Enter your guess: "))
            used_attempts += 1
            attempts -= 1

            if guess == secret_number:
                print(f" Correct! You guessed it in {used_attempts} attempts.")

                if best_score is None or used_attempts < best_score:
                    best_score = used_attempts
                    print(" New Best Score!")
                break

            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

            if abs(guess - secret_number) <= hint_range:
                print(" You are very close!")

            print("Attempts remaining:", attempts)

        else:
            print(f"\n Game Over! The number was {secret_number}")

        if best_score is not None:
            print("Best Score:", best_score)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

    except ValueError:
        print("Invalid input! Please enter numbers only.")
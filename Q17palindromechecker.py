try:
    user_input = input("Enter word/number: ")

    original = user_input
    processed = user_input.lower()
    reversed_text = processed[::-1]

    print("\nOriginal:", original)
    print("Reversed:", original[::-1])

    print("\nStep-by-step comparison:")

    is_palindrome = True

    for i in range(len(processed)):
        print(f"{processed[i]} == {reversed_text[i]}")
        if processed[i] != reversed_text[i]:
            is_palindrome = False

    if is_palindrome:
        print("\nResult: PALINDROME")
    else:
        print("\nResult: NOT A PALINDROME")

except Exception:
    print("Something went wrong. Please try again.")

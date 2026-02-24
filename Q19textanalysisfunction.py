def count_words(text):
    words = text.split()
    return len(words)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    processed = text.replace(" ", "").lower()
    return processed == processed[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def analyze_text(text):
    print("\nTEXT ANALYSIS")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    if longest:
        print("Longest word:", longest, f"({len(longest)} letters)")
    else:
        print("Longest word: None")

    freq = word_frequency(text)
    print("Word Frequency:")
    for word, count in freq.items():
        print(f"{word}: {count}")

user_text = input("Enter text: ")
analyze_text(user_text)

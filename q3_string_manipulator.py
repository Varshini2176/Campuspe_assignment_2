sentence = input("Enter a sentence: ")
print("\nOriginal:", sentence)
# Total characters (with spaces)
print("Characters (with spaces):", len(sentence))
# Total characters (without spaces)
print("Characters (without spaces):", len(sentence.replace(" ", "")))
# Total words
words = sentence.split()
print("Words:", len(words))
# uppercase
print("UPPERCASE:", sentence.upper())
# lowercase
print("lowercase:", sentence.lower())
# Title Case
print("Title Case:", sentence.title())
# first word
if len(words) > 0:
    print("First word:", words[0])
else:
    print("First word: None")
# last word
if len(words) > 0:
    print("Last word:", words[-1])
else:
    print("Last word: None")
# Reversed sentence
print("Reversed:", sentence[::-1])
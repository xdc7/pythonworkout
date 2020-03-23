"""
Handle punctuation in piglatin: If a word ends with punctuation, then that should be shifted to the end of the translated word.
"""

word = input ("Enter a word...\n")
punctuation = ""

if word[-1] in "!.'\"":
    punctuation = word[-1]
    word = word[:-1]

if word[0] in "aeiou":
    result = f"{word}way{punctuation}"
else:
    result = f"{word[1:]}{word[0]}ay{punctuation}"

print(result)
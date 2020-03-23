"""
Consider an alternative version of Pig Latin, in which we don't check to see if the first letter is a vowel, but rather we check to see if the word contains two different vowels. Thus, 'wine' would have 'way' added to the end, but 'wind' would be translated into 'indway'. How would you check for two different vowels in the word? (Hint: Sets can come in handy here.)
"""
def wordToAlternativePigLatin(word):
    if len(word) < 1:
        return ""
    vowels = set('aeiou')
    if len(vowels.intersection(word)) >= 2:
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"






print (wordToAlternativePigLatin('air'))
print (wordToAlternativePigLatin('mist'))
print (wordToAlternativePigLatin('eat'))
print (wordToAlternativePigLatin('python'))
print (wordToAlternativePigLatin('computer'))
print (wordToAlternativePigLatin('a'))
print (wordToAlternativePigLatin('b'))


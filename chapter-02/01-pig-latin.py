"""write a Python program that asks the user to enter an English word. Your program should then print the word, translated into Pig Latin. You may assume that the word contains no capital letters or punctuation.

# How to translate a word to pig latin:

* If the word begins with a vowel (a, e, i, o, or u), then add way to the end of the word. So air becomes airway and eat becomes eatway . 

* If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add ay . Thus, python becomes ythonpay and computer becomes omputercay .

"""

def wordToPiglatin(word):
    if len (word) < 1:
        return None
    word = word.lower()
    result = ''
    if word[0] in 'aeiou':
            result = word + 'way'
    else:
        result = word[1:] + word[0] + 'ay'
    return result



print (wordToPiglatin('air'))
print (wordToPiglatin('eat'))
print (wordToPiglatin('python'))
print (wordToPiglatin('computer'))
print (wordToPiglatin('a'))
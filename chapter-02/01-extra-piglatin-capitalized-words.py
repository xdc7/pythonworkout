"""
Handle capitalized words: If a word is capitalized (i.e., the first letter is capitalized, but the rest of the word isn’t), then the Pig Latin translation should be similarly capitalized.

"""
def wordToPiglatin(word):
    if len (word) < 1:
        return None
    startwithUpperCase = False
    if ord(word[0]) >= 65 and  ord(word[0]) <= 90:
    	startwithUpperCase = True
    result = ''
    if word[0] in 'aeiou' or word[0] in 'AEIOU':
            result = word + 'way'
    else:
        result = word[1:] + word[0] + 'ay'
        if startwithUpperCase:
        	result = result[0].upper() + result[1:].lower()
    return result


print (wordToPiglatin('b'))
print (wordToPiglatin('a'))
print (wordToPiglatin('air'))
print (wordToPiglatin('Eat'))
print (wordToPiglatin('Python'))
print (wordToPiglatin('computer'))
print (wordToPiglatin('a'))
print (wordToPiglatin('B'))
print (wordToPiglatin('Aa'))


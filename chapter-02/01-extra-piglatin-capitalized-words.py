"""
Handle capitalized words: If a word is capitalized (i.e., the first letter is capitalized, but the rest of the word isn’t), then the Pig Latin translation should be similarly capitalized.

"""
def wordToPiglatin(word):
    if len (word) < 1:
        return None
    startwithUpperCase = False
    if ord(word[0]) >= 65 and  ord(word[0]) <= 90:
    	startwithUpperCase = True    	
    lowerCaseWord = word.lower()
    result = ''
    if lowerCaseWord[0] in 'aeiou':
            result = word + 'way'
    else:
        result = lowerCaseWord[1:] + lowerCaseWord[0] + 'ay'
        if startwithUpperCase:
        	upperCaseResult = []
        	for i, c in enumerate(result):
        		upperCaseResult.append(result[i]) 
        	upperCaseResult[0] = upperCaseResult[0].upper()
        	result = ''.join(upperCaseResult) 	
        	
        	 # result[0].upper() + result[1:]
    return result


print (wordToPiglatin('b'))
print (wordToPiglatin('a'))
print (wordToPiglatin('air'))
print (wordToPiglatin('Eat'))
print (wordToPiglatin('Python'))
print (wordToPiglatin('computer'))
print (wordToPiglatin('a'))
print (wordToPiglatin('B'))


"""
Given a list of strings, sort them according to how many vowels they contain.

"""
   
from operator import itemgetter, attrgetter

def vowelCounter(textString):
	result = 0
	if not textString:
		return result
	for c in textString.lower():
		if c in 'aeiou':
			result += 1
	return result

def sortListByNumberOfVowels(listOfStrings):
	
	result = sorted(listOfStrings, key= vowelCounter, reverse=True)
	return result

	
l1 = ['Aaron', 'Beckham', 'Maldini', 'AAAa', 'ZZtop', 'aeiou']	    


print(sortListByNumberOfVowels(l1))


# print (vowelCounter('ndssopodsf3qwexc'))
# print (vowelCounter('aeiou'))
# print (vowelCounter(''))
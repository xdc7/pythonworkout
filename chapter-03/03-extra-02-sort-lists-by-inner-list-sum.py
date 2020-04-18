"""
Given a list of lists, with each list containing zero or more numbers, sort by the sum of each inner list’s numbers.
"""
   
from operator import itemgetter, attrgetter

def listSummer(listOfNumbers):
	result = 0
	if not listOfNumbers:
		return result
	for n in listOfNumbers:
			result += n
	return result

def sortListByInnerListSums(listOfNumberLists):
	
	result = sorted(listOfNumberLists, key= listSummer)
	return result

	
l1 = [
	[1,2,30,],
	[1,2,3,4,5],
	[1,2],
	[1,2,3,4],
]	    



print(sortListByInnerListSums(l1))


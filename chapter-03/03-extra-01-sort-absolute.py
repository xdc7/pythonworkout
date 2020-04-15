"""
Given a sequence of positive and negative numbers, sort them by absolute value.

"""
   
from operator import itemgetter, attrgetter

def sortListOfNmbersAbsolute(listOfNumbers):
	
	result = sorted(listOfNumbers, key= abs)
	return result

	
l1 = [-1,2,-3,4,-5,9,-8 ]	    
l2 = [-5,1,9,-2,-1 ]	    


print(sortListOfNmbersAbsolute(l1))
print(sortListOfNmbersAbsolute(l2))

"""
Write a function that takes a float and two integers (before and after). The function should return a float consisting of before digits before the decimal point and after digits after. Thus if we call the function with 1234.5678, 2 and 3, the return value should be 34.567.
"""

def floatBeforeAfter(floatNum, int01, int02):
	strRep = str(floatNum)
	if '.' not in strRep:
		return False
	indexOfPeriod = strRep.index('.')
	firstPart = strRep[0:indexOfPeriod]
	secondPart = strRep[indexOfPeriod+1:]
	if (len(firstPart) < int01 or len(secondPart) < int02):
		return False
	return (f'float: {floatNum} first part: {firstPart[-int01:]} --- second part {secondPart[:int02]}')
	
	
		
	
print(floatBeforeAfter(1234.5678,2,3))
print(floatBeforeAfter(14.567,2,3))
print(floatBeforeAfter(1.567,1,4))

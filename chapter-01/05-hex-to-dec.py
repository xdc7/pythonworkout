"""
Write a program that takes a hex number and returns the decimal equivalent. That is, if the user enters 50, then we will assume that it is a hex number (equal to 0x50), and will print the value 80 on the screen. And no, you shouldn’t convert the number all at once using the int function, although it is permissible to use int one digit at a time.
"""


def hexToDec(userInput):
	userInput = list(str(userInput))
	userInput.reverse()
	result = 0
	for i, digit in enumerate(userInput):
		temp = 0
		if digit.upper() == 'A':
			temp = 10
		elif digit.upper() == 'B':
			temp = 11
		elif digit.upper() == 'C':
			temp = 12
		elif digit.upper() == 'D':
			temp = 13
		elif digit.upper() == 'E':
			temp = 14
		elif digit.upper() == 'F':
			temp = 15
		else:
			temp = int(digit)					
		tempResult = temp * 16 ** i
		result += tempResult
	return result

print(hexToDec(50))

print(hexToDec('ABC'))

print(hexToDec(0))
		
		


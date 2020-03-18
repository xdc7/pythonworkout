"""
Write a program that takes a hex number and returns the decimal equivalent. That is, if the user enters 50, then we will assume that it is a hex number (equal to 0x50), and will print the value 80 on the screen. Implement the above program such that it doesn’t use the int function at all, but rather uses the builtin ord and chr functions to identify the character. This implementation should be more robust, ignoring characters that aren’t legal for the entered number base.
"""


def hexToDec(userInput):
	userInput = list(str(userInput))
	userInput.reverse()
	result = 0
	for i, digit in enumerate(userInput):
		temp = 0
		if (ord(digit) >= 48 and ord(digit) <= 57) or (ord(digit) >= 65 and ord(digit) <= 70) or (ord(digit) >= 97 and ord(digit) <= 102):
			if ord(digit) == 48:
				temp = 0
			elif ord(digit) == 49:
				temp = 1
			elif ord(digit) == 50:
				temp = 2
			elif ord(digit) == 51:
				temp = 3
			elif ord(digit) == 52:
				temp = 4
			elif ord(digit) == 53:
				temp = 5
			elif ord(digit) == 54:
				temp = 6
			elif ord(digit) == 55:
				temp = 7
			elif ord(digit) == 56:
				temp = 8
			elif ord(digit) == 57:
				temp = 9
			elif ord(digit) == 65 or ord(digit) == 97:
				temp = 10
			elif ord(digit) == 66 or ord(digit) == 98:
				temp = 11
			elif ord(digit) == 67 or ord(digit) == 99:
				temp = 12
			elif ord(digit) == 68 or ord(digit) == 100:
				temp = 13
			elif ord(digit) == 69 or ord(digit) == 101:
				temp = 14
			elif ord(digit) == 70 or ord(digit) == 102:
				temp = 15
		else:
			return "Invalid hexadecimal number"					
		tempResult = temp * 16 ** i
		result += tempResult
	return result

print(hexToDec(50))

print(hexToDec('ABC'))

print(hexToDec(0))

print(hexToDec('FEDC134'))
		
		


"""
Write a function that transposes a list of strings, in which each string contains multiple words separated by whitespace. So if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz'] to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].

[
'abc def ghi', 
'jkl mno pqr', 
'stu vwx yz'
]

[
'abc jkl stu', 
'def mno vwx', 
'ghi pqr yz'
]

"""

import unittest

def stringListTranspose(listOfStrings):
	result = []
	for i in range(0, len(listOfStrings)):
		tmp = []
		for j in range(0,len(listOfStrings)):
			tmp.append(listOfStrings[j].split()[i])
		result.append(' '.join(tmp))
	return result
	

			
class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(stringListTranspose([]), [])
    
    def test_valid01(self):
        self.assertEqual(stringListTranspose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']), ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'])
    
    def test_valid02(self):
        self.assertEqual(stringListTranspose(['abcd defg ghij', 'jklm mnop pqrs', 'stuv vwxy yz']), ['abcd jklm stuv', 'defg mnop vwxy', 'ghij pqrs yz'])
    
    # def test_invalid(self):
    #     self.assertEqual(mysum(1,2,'d',3), ValueError)

    # def test_positive(self):
    #     self.assertEqual(mysum(1,2,4,3), 10)

    # def test_negative(self):
    #     self.assertEqual(mysum(1,2,-4,3), 2)
    
    # def test_list(self):
    #     self.assertEqual(mysum(*[1,2,4,3]), 10)

if __name__ == '__main__':
    unittest.main()

"""
Write a function that takes any even number of arguments and returns a dict based on them. The even-indexed arguments become the dict keys, while the odd-numbered arguments become the dict values. Thus, calling the function with the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being returned.
"""

import unittest

def makeDictOddEven(*args):
	result ={}
	for i in range(0,len(args),2):
		result[args[i]] = args[i+1] 
	return result


d1 = ('a', 1, 'b', 2)
d1 = ('a', 1, 'b', 2, 'c', 3)
# d2 = {'a':1, 'b':2, 'c':4}
# d3 = {'a':1, 'b':2, 'd':3}
# d4 = {'a':1, 'b':2, 'c':4}
# d5 = {'a':1, 'b':2, 'd':4}

class TestmakeDictOddEven(unittest.TestCase):

    def test_valid01(self):
        self.assertEqual(makeDictOddEven('a', 1, 'b', 2), {'a':1, 'b':2})
    def test_valid02(self):
        self.assertEqual(makeDictOddEven('a', 1, 'b', 2, 'c', 3), {'a':1, 'b':2, 'c':3})
    # def test_valid03(self):
    #     self.assertEqual(makeDictOddEven(d3, d4), {'a':1, 'b':2, 'd':3, 'c':4})
    # def test_valid04(self):
    #     self.assertEqual(makeDictOddEven(d1, d5), {'a':1, 'b':2,'c':3,  'd':4})
    
    
if __name__ == '__main__':
    unittest.main()

"""
The dict.update method merges two dicts. Write a function that takes any number of dicts, and returns a dictionary that reflects the combination of all of them. If the same key appears in more than one dictionary, then the most recently merged dict’s value should appear in the output.

"""

import unittest


def combinedicts(*argv):
	result = {}
	for item in argv:
		result.update(item)
	return result


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}

class Testcombinedicts(unittest.TestCase):

    def test_valid01(self):
        self.assertEqual(combinedicts(d1, d1), d1)
    def test_valid02(self):
        self.assertEqual(combinedicts(d1, d2), {'a':1, 'b':2, 'c':4})
    def test_valid03(self):
        self.assertEqual(combinedicts(d3, d4), {'a':1, 'b':2, 'd':3, 'c':4})
    def test_valid04(self):
        self.assertEqual(combinedicts(d1, d5), {'a':1, 'b':2,'c':3,  'd':4})
    
    
if __name__ == '__main__':
    unittest.main()

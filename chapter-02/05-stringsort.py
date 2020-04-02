"""
In this exercise, you’ll explore this idea by writing a function, strsort, that takes a single string as its input, and returns a string. The returned string should contain the same characters as the input, except that its characters should be sorted in order, from smallest Unicode value to highest Unicode value.

    For example, the result of invoking strsort('cba') will be the string abc.
    
"""
import unittest


def strsort(inputString):
	return ''.join(sorted(inputString))
	
	


class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(strsort(''), '')

    def test_valid01(self):
        self.assertEqual(strsort('abc'), 'abc')

    def test_valid02(self):
        self.assertEqual(strsort('cba'), 'abc')

    def test_valid03(self):
        self.assertEqual(strsort('defjam'), 'adefjm')

    def test_valid04(self):
        self.assertEqual(strsort('bcfa'), 'abcf')





if __name__ == '__main__':
    unittest.main()

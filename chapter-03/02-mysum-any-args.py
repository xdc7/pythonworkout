"""
This challenge asks you to redefine the mysum function we defined in chapter 1, such that it can take any number of arguments. The arguments must all be of the same type and know how to respond to the + operator. (Thus, the function should work with numbers, strings, lists, and tuples, but not with sets and dictionaries.)
The result should be a new, longer sequence of the type provided by the parameters. Thus, the result of mysum('abc', 'def') will be the string abcdef , and the result of mysum([1,2,3], [4,5,6]) will be the six-element list [1,2,3,4,5,6] . Of course, it should also still return the integer 6 if we invoke mysum(1,2,3)
"""

import unittest

def mysum(*args):
    if not args:
        return args
    result = args[0]
    for item in args[1:]:
        result += item
    return result



			
class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(mysum(), ())
    
    def test_valid01(self):
        self.assertEqual(mysum('abc', 'def'), 'abcdef')
    
    def test_valid02(self):
        self.assertEqual(mysum([1,2,3], [4,5,6]), [1,2,3,4,5,6])
    
    def test_valid03(self):
        self.assertEqual(mysum(1,2,3), 6)
    
    def test_valid04(self):
        self.assertEqual(mysum(1), 1)
    
    def test_valid05(self):
        self.assertEqual(mysum([1], ), [1])

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

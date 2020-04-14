"""
Write a function that partly emulates the builtin zip function ( docs.python.org/3/library/functions.html#zip ), taking any number of iterables and returning a list of tuples. Each tuple will contain one element from each of the iterables passed to the function. Thus, if I call myzip([10, 20,30], 'abc') , the result will be [(10, 'a'), (20, 'b'), (30, 'c')] . You can return a list (not an iterator), and can assume that all of the iterables are of the same length.
"""

import unittest

def myzip(*args):
    result = []
    for i in range(0, len(args[0])):
       temp = []
       for j in range(0, len(args[0])):
           if j < len(args):
               temp.append(args[j][i])
       result.append(tuple(temp))
    return result


# Unit tests
        
class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(myzip(''), [])
    
    def test_valid01(self):
        self.assertEqual(myzip([10, 20,30], 'abc') , [(10, 'a'), (20, 'b'), (30, 'c')])
    
    def test_valid02(self):
        self.assertEqual(myzip([10,20,30,40], 'abcd', (1,2,3,4)) , [(10, 'a', 1), (20, 'b', 2), (30, 'c', 3), (40, 'd', 4)])



if __name__ == '__main__':
    unittest.main()
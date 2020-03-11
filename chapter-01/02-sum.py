import unittest

def mysum(*args):
    """ Implements a simple sum function"""
    result = 0
    for i in args:
        if (not isinstance(i, int)):
            return ValueError
        result += i
    return result






class Testmysum(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(mysum(), 0)
    
    def test_invalid(self):
        self.assertEqual(mysum(1,2,'d',3), ValueError)

    def test_positive(self):
        self.assertEqual(mysum(1,2,4,3), 10)

    def test_negative(self):
        self.assertEqual(mysum(1,2,-4,3), 2)
    
    def test_list(self):
        self.assertEqual(mysum(*[1,2,4,3]), 10)

if __name__ == '__main__':
    unittest.main()
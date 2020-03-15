import unittest

def mysum(numberList=[],startingPoint=0):
    """ Implements a simple sum function with an optional starting point. Note that the function takes a list as the first parameter"""
    if len(numberList) == 0:
        return 0
    result = 0
    for num in numberList:
        if (not isinstance(num, int)):
            return ValueError
        result += num
    return result






class Testmysum(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(mysum(), 0)
    
    def test_invalid(self):
        self.assertEqual(mysum([1,2,'d',3],5), ValueError)

    def test_positive(self):
        self.assertEqual(mysum([1,2,4,3],5), 10)
    
    def test_positive_no_starting_point(self):
        self.assertEqual(mysum([1,2,4,3]), 10)

    def test_negative(self):
        self.assertEqual(mysum([1,2,-4,3]), 2)
    
    # def test_list(self):
    #     self.assertEqual(mysum(*[1,2,4,3],5), 10)

if __name__ == '__main__':
    unittest.main()
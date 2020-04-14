"""
Write a function, mysum_bigger_than , which works the same as mysum , except that it takes a first argument, preceding *args . That argument indicates the threshold for including an argument in the sum. Thus, calling mysum_bigger_than(10, 5, 20, 30, 6) would return 50 — because 5 and 6 aren’t greater than 10 . This function should similarly work with any types, and assumes that all of the arguments are of the same type. Note that > and < work on many different types in Python, not just on numbers; with strings, lists, and tuples, it refers to their sort order.
"""

import unittest

def mysum_bigger_than(*args):
    if not args:
        return args
    threshold = args[0]
    # capture the type of the argument
    temp = type(threshold)
    # create a blank variable using the argument's type
    result = temp()
    for item in args[1:]:
        if item > threshold:
            result += item
    return result

    # Inefficient, easier solution that uses 2 loops

    # threshold = args[0]
    # result = []
    # for item in args[1:]:
    #     if item > threshold:
    #         result.append(item)
    
    # output = result[0]
    # for item in result[1:]:
    #     output += item
    # return output


			
class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(mysum_bigger_than(), ())
    
    def test_valid01(self):
        self.assertEqual(mysum_bigger_than(10, 5, 20, 30, 6), 50)
    
    def test_valid02(self):
        self.assertEqual(mysum_bigger_than('b', 'a' ,'b', 'c'), 'c')
    
    def test_valid03(self):
        self.assertEqual(mysum_bigger_than([1,2,3] , [1,2,3], [4,5,6], [7, 8, 9]), [4,5,6,7,8,9])
    
    # def test_valid03(self):
    #     self.assertEqual(mysum(1,2,3), 6)
    
    # def test_valid04(self):
    #     self.assertEqual(mysum(1), 1)
    
    # def test_valid05(self):
    #     self.assertEqual(mysum([1], ), [1])

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

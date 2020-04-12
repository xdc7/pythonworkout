"""
Write a function, sum_numeric , which takes any number of arguments. If the argument is or can be turned into an integer, then it should be added to the total. Those arguments which cannot be handled as integers should be ignored. The result is the sum of the numbers. Thus, sum_numeric(10, 20, 'a','30', 'bcd') would return 60 . Notice that even if the string 30 is an element in the list, it’s converted into an integer and added to the total.
"""

import unittest

def sum_numeric(*args):
    if not args:
        return args
    result = 0

    for item in args:
        try:
            item = int(item)
            result += item
        except Exception as error:
            print(f"{error}: {item} is not an integer or couldn't be converted into an integer")
    return result



			
class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(sum_numeric(), ())
    
    def test_valid01(self):
        self.assertEqual(sum_numeric(10, 20, 'a','30', 'bcd'), 60)
    
    # def test_valid02(self):
    #     self.assertEqual(mysum_bigger_than('b', 'a' ,'b', 'c'), 'c')
    
    # def test_valid03(self):
    #     self.assertEqual(mysum_bigger_than([1,2,3] , [1,2,3], [4,5,6], [7, 8, 9]), [4,5,6,7,8,9])
    
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

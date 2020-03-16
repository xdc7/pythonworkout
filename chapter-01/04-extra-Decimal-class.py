"""
Explore the Decimal class (docs.python.org/3.7/library/decimal.html), which has an alternative floating-point representation that’s as accurate as any decimal number can be. Write a function that takes two strings from the user, turns them into Decimal instances, and then prints the floating-point sum of the user’s two inputs. In other words, make it possible for the user to enter 0.1 and 0.2, and for us to get 0.3 back.
"""

from decimal import *
import unittest

def sumUsingDecimalClass(str01,str02):	
	try:
		result = Decimal(str01) + Decimal(str02)
		return result
	except:
		return None


print(f'Decimal class precision info\n: {getcontext()}')

# str01 = str(input('Enter the first number'))
# str02 = str(input('Enter the second number'))
# print (f'The answer is:  {sumUsingDecimalClass(str01,str02)}')


class Testmysum(unittest.TestCase):

    def test_invalid(self):
        self.assertEqual(sumUsingDecimalClass('0.1', '0.f2'), None)
    
    def test_positive01(self):
        self.assertEqual(sumUsingDecimalClass('0.1', '0.2'), Decimal('0.3'))
    
    def test_negative01(self):
        self.assertEqual(sumUsingDecimalClass('-0.1', '0.2'), Decimal('0.1'))                

    # def test_invalid(self):
    #     self.assertEqual(mysum(1,2,'d',3), ValueError)
    # 
    # def test_positive(self):
    #     self.assertEqual(mysum(1,2,4,3), 10)
    # 
    # def test_negative(self):
    #     self.assertEqual(mysum(1,2,-4,3), 2)
    # 
    # def test_list(self):
    #     self.assertEqual(mysum(*[1,2,4,3]), 10)

if __name__ == '__main__':
	unittest.main()

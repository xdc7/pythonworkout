"""
Write a function that takes a list or tuple of numbers. Return the result of alternately adding and subtracting numbers from each other. So calling the function as plus_minus([10, 20, 30, 40, 50, 60]) , you’ll get back the result of 10+20-30+40-50+60 , or 50 .
"""

import unittest

def plus_minus(sequence):
    sumResult = 0
    for i in range (0, len(sequence)):
        if i % 2 == 0 and i != 0:
            sumResult = sumResult - sequence[i]
        else:
            sumResult = sumResult + sequence[i]
    return sumResult
print(plus_minus([10, 20, 30, 40, 50, 60]))
print(plus_minus([10, -20, 30, 40, -50, 60]))
print(plus_minus([-10, 20, 30, 40, 50, 60]))
print(plus_minus([10, 20, 30, 40, -50, 60]))

# class TeststringListTranspose(unittest.TestCase):

#     def test_blank(self):
#         self.assertEqual(even_odd_sums(''), [0,0])
    
#     def test_valid01(self):
#         self.assertEqual(even_odd_sums([10, 20, 30, 40, 50, 60]) , [90, 120])

#     # def test_valid02(self):
#     #     self.assertEqual(even_odd_sums('Beckham Zidane Maldini Aguero Lampard'), 'Aguero,Beckham,Lampard,Maldini,Zidane')



# if __name__ == '__main__':
#     unittest.main()
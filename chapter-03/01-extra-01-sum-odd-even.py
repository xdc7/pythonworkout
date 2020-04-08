"""
Write a function that takes a list or tuple of numbers. Return a two-element list, containing (respectively) the sum of the even-indexed numbers and the sum of the odd-indexed numbers. So calling the function as even_odd_sums([10, 20, 30, 40, 50, 60]) , you’ll get back [90, 120]
"""

import unittest

def even_odd_sums(sequence):
    sumOdd = 0
    sumEven = 0
    for i in range (0, len(sequence)):
        if i % 2 == 0:
            sumEven += sequence[i]
        else:
            sumOdd += sequence[i]
    return [sumEven, sumOdd]


class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(even_odd_sums(''), [0,0])
    
    def test_valid01(self):
        self.assertEqual(even_odd_sums([10, 20, 30, 40, 50, 60]) , [90, 120])

    # def test_valid02(self):
    #     self.assertEqual(even_odd_sums('Beckham Zidane Maldini Aguero Lampard'), 'Aguero,Beckham,Lampard,Maldini,Zidane')



if __name__ == '__main__':
    unittest.main()
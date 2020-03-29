"""
In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub . Thus milk becomes mubilk ( m-ub-ilk ) and program becomes prubogrubam ( prub-ogrub-am ).
For this exercise, you’ll translate a word from English into Ubbi Dubbi. So if the user enters octopus , you’ll output uboctubopubus . And if the user enters elephant , you’ll output ubelubephubant .
"""

import unittest

def wordToUbbiDubbi(word):
    if len(word) < 1:
        return ''
    result = []
    for letter in word:
        if letter in 'aeiou':
            result.append('ub')
        result.append(letter)
    return ''.join(result)



class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(wordToUbbiDubbi(''), '')
    
    def test_valid01(self):
        self.assertEqual(wordToUbbiDubbi('milk'), 'mubilk')
        
    def test_valid02(self):
        self.assertEqual(wordToUbbiDubbi('program'), 'prubogrubam')
    
    def test_valid03(self):
        self.assertEqual(wordToUbbiDubbi('octopus'), 'uboctubopubus')
    
    def test_valid04(self):
        self.assertEqual(wordToUbbiDubbi('utopia'), 'ubutubopubiuba')
    
    
    


if __name__ == '__main__':
    unittest.main()

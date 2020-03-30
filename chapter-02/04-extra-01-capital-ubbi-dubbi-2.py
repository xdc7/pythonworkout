"""
Handle capitalized words: If a word is capitalized (i.e., the first letter is capitalized, but the rest of the word isn’t), then the Ubbi Dubbi translation should be similarly capitalized.

In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub . Thus milk becomes mubilk ( m-ub-ilk ) and program becomes prubogrubam ( prub-ogrub-am ).
For this exercise, you’ll translate a word from English into Ubbi Dubbi. So if the user enters octopus , you’ll output uboctubopubus . And if the user enters elephant , you’ll output ubelubephubant .

"""

import unittest

def wordToUbbiDubbi(word):
	if len(word) < 1:
		return ''
	result = []
	upperCase = False
	if word[0].isupper():
		upperCase = True
	word = word.lower()
	for letter in word:
		if letter in 'aeiou':
			result.append('u')
			result.append('b')
		result.append(letter)
	if upperCase:
		result[0] = result[0].upper()
	return ''.join(result)
	
	

class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(wordToUbbiDubbi(''), '')
    
    def test_valid01(self):
        self.assertEqual(wordToUbbiDubbi('Milk'), 'Mubilk')
        
    def test_valid02(self):
        self.assertEqual(wordToUbbiDubbi('program'), 'prubogrubam')
    
    def test_valid03(self):
        self.assertEqual(wordToUbbiDubbi('Octopus'), 'Uboctubopubus')
    
    def test_valid04(self):
        self.assertEqual(wordToUbbiDubbi('utopia'), 'ubutubopubiuba')
    
    
    


if __name__ == '__main__':
    unittest.main()

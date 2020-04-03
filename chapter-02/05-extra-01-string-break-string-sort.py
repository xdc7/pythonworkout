"""
Given the string "Tom Dick Harry", break it into individual words, and then sort those words alphabetically. Then print them with commas ( , ) between the names.
"""
import unittest

def sortStringofWords(sentence):
    if len(sentence) < 1:
        return ''
    return ','.join(sorted(sentence.split()))

class TeststringListTranspose(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(sortStringofWords(''), '')
    
    def test_valid01(self):
        self.assertEqual(sortStringofWords('Tom Dick Harry'), 'Dick,Harry,Tom')

    def test_valid02(self):
        self.assertEqual(sortStringofWords('Beckham Zidane Maldini Aguero Lampard'), 'Aguero,Beckham,Lampard,Maldini,Zidane')



if __name__ == '__main__':
    unittest.main()
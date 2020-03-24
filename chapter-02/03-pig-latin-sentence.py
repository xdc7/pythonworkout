"""
Translate a series of English words into Pig Latin. (To make things easier, we won’t actually ask for a real sentence. More specifically, there will be no capital letters or punctuation.) So, if someone were to enter:
this is a test translation
the output would be:
histay isway away esttay ranslationtay

"""
import unittest

def wordToPigLatin(word):
    if len(word) < 1:
        return None
    if word[0] in 'aeiou':
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"

def sentenceToPigLatin(sentence):
    if len(sentence) < 1:
        return ''
    resultList = []
    for word in sentence.split(' '):
        resultList.append(wordToPigLatin(word))
    return ' '.join(resultList)


class TestsentenceToPigLatin(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(sentenceToPigLatin(''), '')
    
    def test_valid01(self):
        self.assertEqual(sentenceToPigLatin('this is a test translation'), 'histay isway away esttay ranslationtay')
    
    def test_valid02(self):
        self.assertEqual(sentenceToPigLatin('enter the lowercase text here'), 'enterway hetay owercaselay exttay erehay')
    
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
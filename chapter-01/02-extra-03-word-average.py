import unittest

def wordAverage(wordList=[]):
    """  Write a function that takes a list of words (strings). It should return a tuple containing three integers, representing the length of the shortest word, the length of the longest word, and the average word length."""
    if len(wordList) == 0:
        return ()
    totalWordLength = 0
    shortestWord = wordList[0]
    longestWord = wordList[0]
    for word in wordList:
        if word < shortestWord:
            shortestWord = word
        elif word > longestWord:
            longestWord = word
        totalWordLength += len(word)
    print (f'shortest word: {shortestWord}')
    print (f'longest word: {longestWord}')
    
    return (len(shortestWord), len(longestWord), round(totalWordLength / len(wordList),3))



print (wordAverage(['test', 'testings']))


class TestwordAverage(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(wordAverage(), ())
    
    def test_valid1(self):
        self.assertEqual(wordAverage(['test']), (4,4,4.0))
    
    def test_valid2(self):
        self.assertEqual(wordAverage(['test','best', 'testings']), (4,8,5.333))
    
    def test_valid3(self):
        self.assertEqual(wordAverage(['test','testings','testingstestings']), (4,16,9.333))

    # def test_positive(self):
    #     self.assertEqual(wordAverage([1,2,4,3],5), 10)
    
    # def test_positive_no_starting_point(self):
    #     self.assertEqual(wordAverage([1,2,4,3]), 10)

    # def test_negative(self):
    #     self.assertEqual(wordAverage([1,2,-4,3]), 2)
    
    # def test_list(self):
    #     self.assertEqual(wordAverage(*[1,2,4,3],5), 10)

if __name__ == '__main__':
    unittest.main()
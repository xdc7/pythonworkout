import unittest

def mysum(numberList=[],startingPoint=0):
    """ Write a function that takes a list of Python objects. Sum the objects that either are integers or can be turned into integers, ignoring the others. """
    if len(numberList) == 0:
        return 0
    result = 0
    for num in numberList:
        try:
            convertedint = int(num)
        except:
            # print (f'{num} is not a integer and will be skipped')
            continue
        result += convertedint
    return result





class Testmysum(unittest.TestCase):

    def test_blank(self):
        self.assertEqual(mysum(), 0)
    
    def test_invalid(self):
        self.assertEqual(mysum([1,2,'d',3]), 6)

    def test_positive(self):
        self.assertEqual(mysum([1,2,4,3],5), 10)
    
    def test_positive_no_starting_point(self):
        self.assertEqual(mysum([1,2,4,3,'z','55z']), 10)

    def test_negative(self):
        self.assertEqual(mysum([1,2,-4,3]), 2)
    
    # def test_list(self):
    #     self.assertEqual(mysum(*[1,2,4,3],5), 10)

if __name__ == '__main__':
    unittest.main()
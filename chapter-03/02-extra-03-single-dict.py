"""
Write a function that takes a list of dictionaries, and returns a single dictionary that combines all of the keys and values. If a key appears in more than one argument, then the value should be a list containing all of the values from the arguments.
"""

import unittest

def combineDict(listOfDicts):
    result = {}
    for d in listOfDicts:
        for k,v in d.items():
            if result.get(k) is None:
                result.setdefault(k,[v])
            else:
                values = result.get(k)
                if v not in values:
                    values.append(v)
                    result.update({k:values})
    print(result)
    return result


			
class TestcombineDict(unittest.TestCase):

    
    
    # def test_blank(self):
    #     self.assertEqual(combineDict(), ())
    
    def test_valid01(self):
        d1 = {'name':'Jack', 'age': 24, 'country':'usa'}
        d2 = {'name':'Ryan', 'age': 25, 'country':'eng'}
        output = {'age': [24, 25], 'country': ['usa', 'eng'], 'name': ['Jack', 'Ryan']}
        self.assertEqual(combineDict([d1,d2]),output)
    
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

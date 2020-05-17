"""
Write a function, dictdiff, that takes two dictionaries as arguments. The function returns a new
dictionary that expresses the difference between the two dictionaries.
If there are no differences between the dictionaries, then dictdiff returns an empty dictionary.
For each key-value pair that differs, the return value of dictdiff will have a key-value pair in
which the value is a list containing the values from the two different dictionaries. If one of the
dictionaries doesn’t contain that key, it should contain None

Thus:

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1, d1)) # Prints {}
print(dictdiff(d1, d2)) # prints {'c': [3, 4]}, because d1 contains c:3 and d2 contains c:4
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3, d4)) # prints {'c': [None, 4], 'd': [3, None]}
d5 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1, d5)) # prints {'c': [3, None], 'd': [None, 4]}, because d1 has c:3 and d5 has d:4

"""
import unittest

def dictdiff(dict01, dict02):
  result = {}
  
  allKeys = dict01.keys() | dict02.keys()

  # for key in allKeys:
  #   if dict01.get(key) and dict02.get(key):
  #     if dict01.get(key) != dict02.get(key):
  #       result[key] = [dict01.get(key), dict02.get(key)]
  #   elif dict01.get(key) and not dict02.get(key):
  #     result[key] = [dict01.get(key), None]
  #   elif not dict01.get(key) and dict02.get(key):
  #     result[key] = [None, dict02.get(key)]

  for key in allKeys:
    if dict01.get(key) != dict02.get(key):
      result[key] = [dict01.get(key) , dict02.get(key)]
  return result


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
d5 = {'a':1, 'b':2, 'd':4}

class Testdictdiff(unittest.TestCase):

    def test_valid01(self):
        self.assertEqual(dictdiff(d1, d1), {})
    def test_valid02(self):
        self.assertEqual(dictdiff(d1, d2), {'c': [3, 4]})
    def test_valid03(self):
        self.assertEqual(dictdiff(d3, d4), {'c': [None, 4], 'd': [3, None]})
    def test_valid04(self):
        self.assertEqual(dictdiff(d1, d5), {'c': [3, None], 'd': [None, 4]})
    
    
if __name__ == '__main__':
    unittest.main()
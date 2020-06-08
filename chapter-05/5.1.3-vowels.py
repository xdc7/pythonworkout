"""
Read through a text file, line by line. Use a dict to keep track of how many times each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.
"""

import sys, os

# Set filePath to a file path else it will be set to use the current file
filePath = sys.argv[0]

try:
  filePath = sys.argv[1]
except:
  pass

# vowels = {
#   'a' : 0,
#   'e' : 0,
#   'i' : 0,
#   'o' : 0,
#   'u' : 0
# }

vowels = {}

with open(filePath) as f:
  for line in f.readlines(): 
    for letter in line:
      if letter in 'aeiou':
        vowels[letter] = vowels.get(letter,0) + 1


print (vowels)
  


  

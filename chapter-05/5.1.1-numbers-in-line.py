"""
Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace surrounded by whitespace) that contain only integers, and sum them.
"""

import sys, os

# Set filePath to a file path else it will be set to use the current file
filePath = sys.argv[0]

try:
  filePath = sys.argv[1]
except:
  pass

result = 0

with open(filePath) as f:
  for line in f.readlines(): 
    lineList = line.strip().split()
    for word in lineList:
      try:
        result += int(word)
      except:
        pass


print (result)
  


  

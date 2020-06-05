"""
Create a text file (using an editor, not necessarily Python) containing two tab-separated
columns, with each column containing a number. Then read through the file you have
created with Python. For each line, multiply each number by the second, and then sum
the results. Ignore any line that doesn’t contain two numeric columns
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
    multiplicationResult = 1
    lineList = line.strip().split()
    if len(lineList) != 2:
      continue
    for num in lineList:
      try:
        multiplicationResult *= int(num)
      except:
        multiplicationResult = 'x'
    if multiplicationResult != 'x':
      result += multiplicationResult
    multiplicationResult = 1


print (result)
  


  

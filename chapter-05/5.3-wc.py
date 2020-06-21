"""

Ask the user to enter the name of a text file, and then (on one line, separated by spaces) words whose frequencies should be counted in that file. Count how many times those words appear in a dictionary, using the user-entered words as the keys, and the counts as the values.

"""

import sys, os

# Set filePath to a file path else it will be set to use the current file
filePath = sys.argv[0]

try:
  filePath = sys.argv[1]
except:
  pass


characterCount = 0
wordCount = 0
lineCount = 0
uniqueWords = {}
# A better way is to use a set instead of a dict
# uniqueWordsSet = set()

with open(filePath) as f:
  for line in f.readlines():
    lineCount += 1
    characterCount += len(line)
    lineList = line.split()
    wordCount += len(lineList)
    for word in lineList:
      uniqueWords[word] = uniqueWords.get(word, 0) + 1
      # A better way is to use a set instead of a dict
      # uniqueWordsSet.update(lineList)  
    


print (f"Number of Characters: {characterCount}")
print (f"Number of Words: {wordCount}")
print (f"Number of Lines: {lineCount}")
print (f"Number of Unique Words: {len(uniqueWords.keys())}")

# A better way is to use a set instead of a dict
# print (f"Number of Unique Words: {len(uniqueWordsSet)}")
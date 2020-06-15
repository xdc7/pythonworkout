"""

Unix systems contain many utility functions. One of the most useful Python. However, your version of wc will return four different types of information about the files: Number of characters (including whitespace) Number of words (separated by whitespace) Number of lines Number of unique words (case sensitive, so "NO" is different from "no") The program should ask the user for the name of an input file, and then produce output for that file.

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
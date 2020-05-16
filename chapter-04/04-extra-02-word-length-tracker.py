"""
Read through a text file on disk. Use a dict to track how many words of each length are in
the file — that is, how many 3-letter words, 4-letter words, 5-letter words, and so forth.
Display your results

"""

import sys, operator

# Uncomment the line below to read the script file as the input text file and comment line 12 or provide a valid file path on line 12
# inputFilePath = sys.argv[0]
inputFilePath = "04-extra-02-word-length-tracker-text-file.txt"

wordTracker = {}

with open (inputFilePath) as f:
  for line in f.readlines():
    for word in line.split():
      if wordTracker.get(len(word)):
        wordTracker[len(word)] += 1
      else:
        wordTracker[len(word)] = 1


sortedList = sorted(wordTracker.items(), key=operator.itemgetter(0)) 

for item in sortedList:
  print(f"Number of {item[0]} letter words: {item[1]}")


"""

Ask the user to enter the name of a text file, and then (on one line, separated by spaces) words whose frequencies should be counted in that file. Count how many times those words appear in a dictionary, using the user-entered words as the keys, and the counts as the values.

"""



filePath = input("Enter a filename...")
words = input("Enter words (separated by spaces) to search in the above file..")
words = words.split()
wordDict = {}
with open(filePath) as f:
  for lines in f.readlines():
    for word in lines.split():
      if word in words:
        wordDict[word] = wordDict.get(word, 0) + 1


print(wordDict)
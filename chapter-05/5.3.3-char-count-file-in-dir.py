"""
Given a directory, read through each file and count the frequency of each letter. (Force letters to be lowercase, and ignore non-letter characters.) Use a dictionary to keep track of the letter frequencies. What are the five most common letters across all of these files?

"""

import os, sys, re

# Function to return the absolute file paths of files in a directory
def getAbsoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

# Set filePath to a file path else it will be set to use the current file
filePath = sys.argv[0]

try:
  filePath = sys.argv[1]
except:
  filePath = '/'.join(filePath.split('/')[0:-1])

alphabetRegex = re.compile(r'([a-zA-Z])')

results = {}
for fileName in getAbsoluteFilePaths(filePath):
    # print(f"fileName: {fileName}-- fileSize: {os.path.getsize(directory)}")
    # print(f"fileName: {fileName}-- fileSize in KB: {os.stat(os.path.dirname(filePath)).st_size / 1024}")
    with open(fileName) as f:
        for line in f.readlines():
            for letter in line.lower():
                if alphabetRegex.search(letter):
                    results[letter] = results.get(letter,0) + 1

for letter, count in sorted(results.items(), key= lambda item: item[1], reverse=True):
    print(f"letter: {letter} --- count: {count}")
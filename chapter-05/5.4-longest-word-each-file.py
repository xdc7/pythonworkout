"""
In this exercise, the user will provide the name of a directory. You are to find the longest word for each file in the directory, returning a dict whose keys are the filenames and whose values are the longest words.
"""

import os, sys

# # Function to return the absolute file paths of files in a directory
# def getAbsoluteFilePaths(directory):
#    for dirpath,_,filenames in os.walk(directory):
#        for f in filenames:
#            yield os.path.abspath(os.path.join(dirpath, f))

# # Function to return the longest word in a file
# def findLongestWordInFile(filePath):
#     longestWord = ''
#     with open(filePath) as f:
#         for line in f.readlines():
#             for word in line.split():
#                 if len(word) > len(longestWord):
#                     longestWord = word
#     return longestWord

# directory = input('Please provide a directory path....\n')
# if not directory:
#     directory = sys.path[0]

# results = {}

# for fileName in getAbsoluteFilePaths(directory):
#     results[fileName] = findLongestWordInFile(fileName)


# for k,v in results.items():
#     print("file: {0:65} -- Longest word: {1:35}".format(k,v))

## Alternative solution using dictionary comprehension and reading the file line by line

def findLongestWordInFile(fileName):
    longestWord = ''
    if os.path.isfile(fileName):
        for line in open(fileName):
            for word in line.split():
                if len(word) > len(longestWord):
                    longestWord = word
        return longestWord


directory = input('Input a directory name...\n')

if not directory:
    directory = sys.path[0]

# Print directly to the console
# print ({fileName: findLongestWordInFile(os.path.join(directory,fileName)) for fileName in os.listdir(directory)}) 

# (sort of) Pretty print
d = {fileName : findLongestWordInFile(os.path.join(directory, fileName)) for fileName in os.listdir(directory) if os.path.isfile(os.path.join(directory,fileName))}

for k,v in d.items():
    print("file: {0:40} -- longestWord: {1:25}".format(k,v))

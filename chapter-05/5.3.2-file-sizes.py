"""
Create a dictionary in which the keys are the names of files on your system, and the values are the sizes of those files. To calculate the size, you can use os.stat ( docs.python.org/3/library/os.html?#os.stat ).

"""

import os

# Function to return the absolute file paths of files in a directory
def getAbsoluteFilePaths(directory):
   for dirpath,_,filenames in os.walk(directory):
       for f in filenames:
           yield os.path.abspath(os.path.join(dirpath, f))

# directory = input('Enter a directory location....\n')

directory = 'C:\\Windows\\System32'



for fileName in getAbsoluteFilePaths(directory):
    print(fileName)
    print(f"fileName: {fileName}-- fileSize: {os.stat(fileName).st_size / 1024} KB")

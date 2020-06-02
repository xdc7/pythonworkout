"""
Use os.listdir (docs.python.org/3/library/os.html?#os.listdir) to get the names of files
in the current directory. What are the different file extensions (i.e., suffixes following the
final . character) that appear in that directory? It’ll probably be helpful to use
os.path.splitext (docs.python.org/3/library/os.path.html?#os.path.splitext)
"""

import sys, os

# Set dir to a directory path else it will be set to the current dir
dir = '.'

try:
  dir = sys.argv[1]
except:
  pass
  

fileTypes = {}

for f in os.listdir(path=dir):
  ext = os.path.splitext(f)[1]
  fileTypes[ext] = fileTypes.get(ext,0) + 1

print (f"files listed under {dir}: {os.listdir(path=dir)}")
print (f" file types: {fileTypes}")
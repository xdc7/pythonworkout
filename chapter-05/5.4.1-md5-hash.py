"""
“Use the hashlib module in the Python standard library, and the md5 function within it, to calculate the MD5 hash for the contents of every file in a user-specified directory. Then print all of the filenames and their MD5 hashes.”
"""

import os, sys, hashlib

directory = input('Provide a directory path...\n')

if not directory:
    directory = sys.path[0]

for fileName in os.listdir(directory):
    fullFilePath = os.path.join(directory,fileName)
    if (os.path.isfile(fullFilePath)):
        with open(fullFilePath, 'rb') as f:
            contents = f.read()
            hashValue = hashlib.md5(contents).hexdigest()
            print("file: {0:45} -- MD5 hash: {1:50}".format(fileName,hashValue))


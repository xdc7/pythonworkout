"""
Ask the user for a directory name. Show all of the files in the directory, as well as how long ago the directory was modified. You will probably want to use a combination of os.stat and the "Arrow" package on PyPI ( pypi.org/project/arrow ) to do this easily.
"""

import sys, os, arrow


directory = input('Provide a directory path...\n')

if not directory:
    directory = sys.path[0]

for fileName in os.listdir(directory):
    fullFilePath = os.path.join(directory,fileName)
    if not os.path.isfile(fullFilePath):
        continue

    # Get the last modified time for the file
    modificationTime = os.stat(fullFilePath).st_mtime

    # Use the arrow library to 'humanize' the modificationTime:
    humanizedModificationTime = arrow.get(modificationTime).humanize()
    print ("File: {0:50} --- Last Modified: {1:30}".format(fileName, humanizedModificationTime))
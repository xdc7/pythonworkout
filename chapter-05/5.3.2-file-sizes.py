"""
Create a dictionary in which the keys are the names of files on your system, and the values are the sizes of those files. To calculate the size, you can use os.stat ( docs.python.org/3/library/os.html?#os.stat ).

"""

import os

directory = input('Enter a directory location....\n')

# directory = 'C:\\Windows\\System32'

for fileName in os.listdir(directory):
    # print(f"fileName: {fileName}-- fileSize: {os.path.getsize(directory)}")
    print(f"fileName: {fileName}-- fileSize in KB: {os.stat(directory).st_size / 1024}")
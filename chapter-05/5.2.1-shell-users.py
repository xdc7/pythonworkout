"""
Read through /etc/passwd , creating a dict in which user login shells (the final field on each line) are the keys. Each value will be a list of the users for whom that shell is defined as their login shell.
"""

import sys, os
from operator import itemgetter, attrgetter

# Set filePath to a file path else it will be set to use the current file
filePath = sys.argv[0]

try:
  filePath = sys.argv[1]
except:
  pass

shells = {}

with open(filePath) as f:
  for line in f.readlines():
    if line.startswith('#'):
      continue
    formattedLine = line.strip().split(':')
    shell = formattedLine[-1]
    user = formattedLine[0]
    if shells.get(shell):
      shells[shell].append(user)
    else:
      shells[shell] = [user]
      
    

sortedShells = sorted(shells.items(),key=itemgetter(0))

for item in sortedShells:
  print(f"shell: {item[0]} users: {item[1]}")
  


  

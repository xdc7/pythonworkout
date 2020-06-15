"""
From /etc/passwd , create a dict in which the keys are the usernames (as in the main exercise), and the values are themselves dicts with keys (and appropriate values) for user ID, home directory, and shell.
"""

import sys, os
from operator import itemgetter, attrgetter

# Set filePath to a file path else it will be set to use the current file
filePath = sys.argv[0]

try:
  filePath = sys.argv[1]
except:
  pass

users = {}

with open(filePath) as f:
  for line in f.readlines():
    if line.startswith('#'):
      continue
    formattedLine = line.strip().split(':')
    if len(formattedLine) < 5:
        continue
    
    user = formattedLine[0]
    userId = formattedLine[2]
    shell = formattedLine[-1]
    homeDir = formattedLine[-2]
    
    users[user] = {'userId': userId, 'shell':shell, 'homeDir': homeDir}  

for user, vals in sorted(users.items()):
    print (f"user: {user} -- values: {vals}")
  

"""
For this exercise, create a dictionary based on /etc/passwd , in which the dict’s keys are usernames and the values are the users' IDs. Once you have created the dictionary, iterate over it, displaying the usernames and associated IDs in alphabetical order.
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
    users[formattedLine[0]] = formattedLine[2]


sortedUsers = sorted(users.items(),key=itemgetter(0))

for item in sortedUsers:
  print("user: {0:25} ID: {1:10}".format(item[0],item[1]))
  


  

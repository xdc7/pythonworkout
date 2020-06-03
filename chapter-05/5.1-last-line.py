"""
In this exercise, you should ask the user for the name of a text file. The program then prints the file’s final line on the screen
"""


# fileName = input('Enter a filename....')

fileName = './5.1-last-line.py'
with open(fileName) as f:
  lastLine = f.readlines()[-1]
  print(lastLine)
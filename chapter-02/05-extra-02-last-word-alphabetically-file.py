"""
Which is the last word, alphabetically, in a text file?
you may well want to read up on the key parameter, and the types of values you can pass to it. A good introduction, with examples, is here: docs.python.org/3/howto/sorting.html#sortinghowto
"""

def lastWordFn(line):
  return (sorted(line.split()))[-1]
lastWord = ''
with open('05-extra-02-last-word-alphabetically-file.txt') as f:
    lines = f.readlines()
    x = sorted(lines,key= lastWordFn)
    lastLine = (sorted(x[-1].split()))
    lastWord = lastLine[-1]
    
    # Another easier way to do the exercise without using the key parameter in the sorted method
    # lastWords = []
    # for line in lines:
    #     lastWords.append(sorted(line.split())[-1])
    # print (sorted(lastWords)[-1])

print (lastWord)
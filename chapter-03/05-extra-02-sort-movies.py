"""
Define a list of tuples, in which each tuple contains the name, length (in minutes), XX -- and director of the movies nominated for "best picture" Oscar awards last year -- XX. Ask the user
whether they want to sort the list by title, length, or director’s name, and then present the
list sorted by the user’s choice of axis.

"""

import operator, collections

# personTuple = collections.namedtuple('personTuple', 'firstName lastName duration')

def printTuple(movies,choice):	
  # for movie in sorted(movies, key=operator.itemgetter(1,0)):
  #   print ("{1:10} {0:10} {2:5.2f}".format(*movie)
  index = 0
  if choice.lower() == 'l':
    index = 1
  elif choice.lower() == 'd':
    index = 2
  print ("{0:20} {1:6} {2:15}".format("Title", "Length", "Director"))
  for movie in sorted(movies, key=operator.itemgetter(index)):
    print ("{0:20} {1:6} {2:15}".format(*movie))


movies = [
  ("Avengers: Endgame", 135, "Joe Russo"), 
  ("Knives Out", 170, "Rian Johnson"), 
  ("Parasite", 175, "Bong Joon-ho")
]

choice = input("Do you want to sort the list by title (t), length (l), or director’s name (d)   \n")

printTuple(movies,choice)

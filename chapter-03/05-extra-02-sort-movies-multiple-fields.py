"""
Define a list of tuples, in which each tuple contains the name, length (in minutes), XX -- and director of the movies nominated for "best picture" Oscar awards last year -- XX. Ask the user
whether they want to sort the list by title, length, or director’s name, allowing the user to sort by two or three of these fields, not just one of them. The user can specify the fields by entering them separated by commas; you can use str.split to turn them into a list. Then present the list sorted by the user’s choice of axis

"""

import operator, collections

# personTuple = collections.namedtuple('personTuple', 'firstName lastName duration')

def printTuple(movies,choice):	
  index = 0
  
  d = {
    't' : 0,
    'l' : 1,
    'd' : 2
  }

  l1 = []
  for item in choice.split(","):
    l1.append(d.get(item))

  
  print ("{0:20} {1:6} {2:15}".format("Title", "Length", "Director"))
  for movie in sorted(movies, key=operator.itemgetter(*l1)):
    print ("{0:20} {1:6} {2:15}".format(*movie))


movies = [
  ("Avengers: Endgame", 135, "Joe Russo"), 
  ("Knives Out", 170, "Rian Johnson"), 
  ("Parasite", 175, "Bong Joon-ho"),
  ("Parasite0", 130, "Bong Joon-ho")
]

choice = input("Do you want to sort the list by title (t), length (l), or director’s name (d)? Enter one, two, or three sorting choices. For example, 't' 't,l', and 't,l,d' are all valid choices   \n")

printTuple(movies,choice)

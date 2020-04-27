"""
For example, assume that we are in charge of an international summit in London. We know how
many hours it will take each of several world leaders to arrive:
3.5 Printing tuple records
def most_repeating_word(words):
word_counts = {word : most_repeating_letter_count(word)
for word in words}
3.4.3 Beyond the exercise
people = [("Donald", "Trump", 7.85),
("Vladimir", "Putin", 3.626),
("Jinping", "Xi", 10.603)]


The planner for this summit needs to have a list of the world leaders who are coming, along with
the time it will take for them to arrive. However, this travel planner doesn’t need the degree of
precision that the computer has provided; it’s enough for us to have two digits after the decimal
point.
For this exercise, write a Python program that takes the above list, and people produces a table
that looks like the following:


Trump Donald 7.85
Putin Vladimir 3.63
Xi Jinping 10.60

Notice that the last name is printed before the first name (taking into account that Chinese names
are generally shown that way), followed by a decimal-aligned indication of how long it will take
for each leader to arrive in London. Each name should be printed in a 10-character field, and the
time should be printed in a 5-character field, with one space character of padding between each
of the columns. Travel time should display only two digits after the decimal point, which means
that even though the input for Xi Jinping’s flight is 10.603 hours, the value displayed should be
10.60.
"""



import operator

def printTuple(people):
  for person in sorted(people, key=operator.itemgetter(1)):
    print ("{1:10} {0:10} {2:5.2f}".format(*person))


people = [("Donald", "Trump", 7.85), ("Vladimir", "Putin", 3.626), ("Jinping", "Xi", 10.603)]

printTuple(people)
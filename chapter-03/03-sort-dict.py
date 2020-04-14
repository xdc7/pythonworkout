"""
Let’s assume that you have phone book data in a list of dictionaries, as follows:

    
      people = [{'first':'Minnie', 'last':'Mouse', 'email':'minnie@mouse.com'},
 {'first':'Donald', 'last':'Duck', 'email':'donald@duck.com'},
 {'first':'Mickey', 'last':'Mouse', 'email':'mickey@mouse.com'}
 ]        
  Let’s assume that you want to print information about all of these people, but in phone-book order — that is, sorted by last name and then by first name. Each line of the output should just look like this:
      
              LastName, FirstName: email@example.com
    
    There are several ways to solve this exercise, but all will require using the sorted method that we saw in the last chapter, along with a function passed as an argument to its key parameter. You can read more about sorted and how to use it, including custom sorts with key, at docs.python.org/3/howto/sorting.html#sortinghowto .

    One of the options for solving this exercise involves operator.itemgetter, about which you can read here: docs.python.org/3/library/operator.html?#operator.itemgetter   
"""
   
from operator import itemgetter, attrgetter

def sortListOfDicts(people):
	# If you want to use a lambda function to sort using just the last name
	# newList = sorted(people, key=lambda person: person['last'])
	
	# Use the itemgetter convenience function to sort using multiple levels (last name and then first name) 
	newList = sorted(people, key=itemgetter('last','first'))
	for person in newList:
		print(f" {person.get('last')}, {person.get('first')}: {person.get('email')}  ")

	
people = [{'first':'Minnie', 'last':'Mouse', 'email':'minnie@mouse.com'},
 {'first':'Donald', 'last':'Duck', 'email':'donald@duck.com'},
 {'first':'Mickey', 'last':'Mouse', 'email':'mickey@mouse.com'}
 ]	    


sortListOfDicts(people)

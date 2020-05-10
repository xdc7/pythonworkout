"""
Define a dictionary whose keys are names of people in your family, and whose values are
their birthdays, as represented by Python date objects (
docs.python.org/3/library/datetime.html?#module-datetime ). Ask the user to enter the
name of someone in your family, and have the program calculate how many days old that person is.


"""

from datetime import datetime      

familyBirthdays = {
  'Jack' : '06/20/1950',
  'Marianne' : '06/05/1963',
  'Alice' : '08/24/1986',
  'Tim' : '02/20/1990',
  'Carrie' : '03/08/2015',
  'Sally' : '05/08/2020',
}

print(f"Family Names: {familyBirthdays.keys()}")

today = datetime.now()

while True:
  print("Enter a person's name from the family above ")
  name = input()
  if not name:
    break
  if name in familyBirthdays:
    birthday = datetime.strptime(familyBirthdays.get(name),'%m/%d/%Y')
    delta = today - birthday
    print(f"{name} is {delta.days} days old")
    

  
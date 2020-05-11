"""
You want to track rainfall in a number of cities. Users of your program will enter the
name of a city; if the city name is blank, then the program exits and prints a report (described
below).
If the city name isn’t blank, then the user should also be asked how much rain has fallen in that
city (typically measured in millimeters). After entering the quantity of rain, the user is again
asked for a city name, rainfall amount, and so on — until the user presses "Enter" instead of
typing the name of a city.
When the user enters a blank city name, the program exits — but first, it reports how much total
rainfall there was in each city. Thus, if I enter

Boston
5
New York
7
Boston
5
[Enter; blank line]

The program should output:
Boston: 10
New York: 7

"""

rainfallTracker = {}

def printReport(rainfallDict):
  for k,v in rainfallDict.items():
    print(f"{k} : {v} ")


while True:
  city = input('Enter a city: ')
  if not city:
    print("\n\nRainfall Report: ")
    printReport(rainfallTracker)
    break
  rainfall = input('Enter the rainfall (in mm) recorded for the city above: ')
  if not rainfall:
    print('Invalid rainfall')
  rainfallTracker[city] = rainfall





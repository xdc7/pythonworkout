"""
You want to track rainfall in a number of cities. Users of your program will enter the
name of a city; if the city name is blank, then the program exits and prints a report (described
below).
If the city name isn’t blank, then the user should also be asked how much rain has fallen in that
city (typically measured in millimeters). After entering the quantity of rain, the user is again
asked for a city name, rainfall amount, and so on — until the user presses "Enter" instead of
typing the name of a city.
When the user enters a blank city name, the program exits — but first, print the total, as well as the average
rainfall for reported days. Thus, if you were to enter 30, 20, and 40 for Boston, you
would see that the total was 90, and that the average was 30.

"""

rainfallTracker = {}

def printReport(rainfallDict):
  for k in rainfallDict.keys():
    
    total = sum(int(item) for item in rainfallDict[k])
    average = total / len(rainfallDict[k])
    print(f"Total Temperatures for {k}: {total}.  Average temperature for {k}: {average}")



while True:
  city = input('Enter a city: ')
  if not city:
    print("\n\nRainfall Report: ")
    printReport(rainfallTracker)
    break
  rainfall = input('Enter the rainfall (in mm) recorded for the city above: ')
  if not rainfall:
    print('Invalid rainfall')
  if rainfallTracker.get(city, 0):
    rainfallTracker[city].append(rainfall)
  else:
    rainfallTracker[city] = [rainfall]





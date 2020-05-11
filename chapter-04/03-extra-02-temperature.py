"""
Define a dict whose keys are dates (represented by strings) from the most recent week,
and whose values are temperatures. Ask the user to enter a date, and display the
temperature on that date, as well as the previous and subsequent dates, if available


"""

      

temperatures = {'05/04/2020' : '70',
              '05/05/2020' : '71',
              '05/06/2020' : '72',
              '05/07/2020' : '73',
              '05/08/2020' : '74',
              '05/09/2020' : '75',
              '05/10/2020' : '76',
}

sortedDates = sorted(temperatures)

while True:
  print("Enter a date in the format MM/DD/YYYY to get the temperature for the day or press enter to quit")
  dateInput = input()
  if not dateInput:
    break
  if dateInput in sortedDates:
    currentTemp = temperatures.get(dateInput)
    print(f"The temperature on {dateInput} was {currentTemp}")
    if sortedDates.index(dateInput) - 1 >= 0:
      previousDateIndex = sortedDates.index(dateInput) - 1
      print(f"The temperature on the day before ({sortedDates[previousDateIndex]}) was {temperatures.get(sortedDates[previousDateIndex])}")
    if sortedDates.index(dateInput) + 1 < len(sortedDates):
      nextDateIndex = sortedDates.index(dateInput) + 1
      print(f"The temperature on the day after will be ({sortedDates[nextDateIndex]}) was {temperatures.get(sortedDates[nextDateIndex])}")

# while True:
#   print('Please enter your username...')
#   userName = input().strip()
#   if not userName:
#     break
#   elif userName not in passwords:
#     print(f'username not found. Please provide your username again')
#     continue
  
#   checkPassword(passwords)
#   break


    

  
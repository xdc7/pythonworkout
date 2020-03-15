"""
Write a program that asks how long it took to run 10 km today. The program continues to ask how long (in minutes) it took for additional runs, until the user enters q . At that point, the program exits — but only after calculating and displaying the average time that the 10 km run took.
"""
totalDistance = 0.0
counter = 0
while True:
    userInput = input('Enter 10 km run time: ')
    if str(userInput).lower() == 'q':
        break
    try:
        userInput = float(userInput)
    except:
        print ('Invalid entry. Please enter the run time in minutes or q to quit')
        continue
    counter += 1
    totalDistance += userInput

if counter > 1:
    averageRunTime = round(totalDistance / counter,3)
    print (f'Your average runing time for 10km based on {counter} entries is {averageRunTime} minutes')

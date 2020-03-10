import random


print ("I'm going guess a number between 0 and 100. Let's see if you can guess it. You have 3 tries. Good Luck!  ")
winningNumber = random.randint(0,100)
counter = 0
success = False
while True:
    userInput = input("Please enter a number between 0 and 100 to see if you guessed right.. ")
    counter += 1
    
    try:
        userInput = int(userInput)
        if (userInput == winningNumber):
            print (f'You guessed it! {userInput} is the number that I had in mind! You win!')
            success = True
            break
        elif (userInput < winningNumber):
            print ('Your number is too low! Try again... ')
        elif (userInput > winningNumber):
            print ('Your number is too high! Try again... ')
    except:
        print (f'{userInput} is not a valid integer. Please try again')
    if (counter == 3):
        print ("Sorry you couldn't guess in 3 tries. Better luck next time")
        break

if (success):
    print (f'It took you {counter} tries to guess the winning number!')
    # print (userInput)


# print (f'The number is {random.randint(1,2)}')
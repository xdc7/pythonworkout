"""
Create a dict in which the keys are usernames and the values are passwords, both
represented as strings. Create a tiny login system, in which the user must enter a
username and password; if there is a match, then indicate that the user has successfully
logged in. If not, then refuse them entry. (Note: This is a nice little exercise, but please
never store unencrypted passwords. It’s a major security risk.)


"""

def checkPassword(passwords):
  passwordRetries = 3
  while passwordRetries > 0:
    passwordRetries -= 1
    print(f'Please enter your password...')
    password = input().strip()
    if password == passwords.get(userName):
      print(f'Welcome to the system, {userName}')
      return True
    else:
      if passwordRetries == 0:
        print(f'Too many incorrect password attemps. Exiting...')
        return False
      print(f'Incorrect password. Please try again. Tries remaining ({passwordRetries})')
      

passwords = {'john' : 'abc1', 'kelly' : 'abc2', 'jane' : 'abc3', 'drew' : 'abc4',}


while True:
  print('Please enter your username...')
  userName = input().strip()
  if not userName:
    break
  elif userName not in passwords:
    print(f'username not found. Please provide your username again')
    continue
  
  checkPassword(passwords)
  break


    

  
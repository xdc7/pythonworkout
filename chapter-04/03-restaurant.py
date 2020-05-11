"""
create a new dictionary, called menu, representing the possible
items you can order at a restaurant. The keys will be strings, and the values will be prices (i.e.,
integers). The program will then ask the user to enter an order:

If the user enters the name of a dish on the menu, then the program prints the price and
the running total. It then asks what else the user wants to order.
If the user enters the name of a dish not on the menu, then the program scolds the user
(mildly). It then asks what else the user wants to order.
If the user enters an empty string, then the program stops asking, and prints the total
amount.
For example, a session with the user might look like this:
Note that you can always check to see if a key is in a dict with the in operator. That returns True

Order: sandwich
sandwich costs 10, total is 10
Order: tea
tea costs 7, total is 17
Order: elephant
Sorry, we are fresh out of elephant today.
Order: <enter>
Your total is 17

"""

menu = {'sandwich' : 10, 'tea' : 7, 'soup' : 9, 'soda' : 4,}

totalBill = 0

while True:
  print('Please enter an item to order and add it to your cart. Just hit enter when you are done ordering')
  choice = input().strip()
  if not choice:
    break
  if choice not in menu:
    print(f'Sorry we are out of fresh {choice}')
    continue
  totalBill += menu.get(choice)

print(f'Your total bill is {totalBill}')
"""Write a program that asks the user for their name, and then produces a "name triangle": The first letter of their name, then the first two letters, then the first three, and so forth, until the entire name is written on the final line."""



def nameTriangle(name):
    for i in range (0, len(name) + 1):
        spaces = ''
        for j in range (0, len(name) -i):
            spaces = spaces + ' '
        print (f'{spaces}{name[0:i]} ')



nameTriangle('James')
nameTriangle('Tim')
nameTriangle('Su')
nameTriangle('Christopher')
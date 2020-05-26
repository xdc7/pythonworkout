"""
In this exercise, you can assume that your Python program contains a list of integers. We want to
print the number of different integers contained within that list. Thus, consider the following:

numbers = [10, 20, 30, 40, 30, 40, 50]

With the above definition, running len(numbers) will return 7, because the list contains 7
elements. How can we get a result of 5, reflecting the fact that the list contains 5 different
values?

"""

numbers = [10, 20, 30, 40, 30, 40, 50]

numbersSet = set(numbers)

print(len(numbersSet))

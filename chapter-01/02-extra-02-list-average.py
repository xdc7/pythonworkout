import unittest

def myaverage(*args):
    """ Implements a simple average function """
    if len(args) == 0:
        return 0
    result = 0
    for num in args:
        if (not isinstance(num, int)):
            return ValueError
        result += num
    return result / len (args)


print(myaverage(*[1,2,3,4]))
print(myaverage(1,2,3,4,5))
print(myaverage(1,1,1))
print(myaverage(0))
print(myaverage())
print(myaverage(5,5,5,5,5,5,5))
print(myaverage(*[1,2,3,4,-6,-50]))





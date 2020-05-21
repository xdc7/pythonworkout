"""
Write a function, dict_partition, that takes one dictionary (d) and a function (f) as
arguments. dict_partition will return two dictionaries, each containing key-value
pairs from d. The decision regarding where to put each of the key-value pairs will be
made according to the output from f, which will be run on each key-value pair in d. If f
returns True, then the key-value pair will be put in the first output dict. If f returns False
, then the key-value pair will be put in the second output dict.

"""

import unittest,random

def dict_partition(d,f):
	result01 ={}
	result02 ={}
	for k,v in d.items():
		if(f(k,v)):
		    result01[k] = v 
		else:
		    result02[k] = v 
	return [result01, result02]

def f(k,v):
	return bool(random.getrandbits(1))


d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print (dict_partition(d1,f))

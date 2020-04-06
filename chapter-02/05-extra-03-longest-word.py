"""
Which is the longest word in a text file?
"""

def sortLongest(ls):
	return sorted(ls.split(), )

with open('05-extra-02-last-word-alphabetically-file.txt') as f:
	lines = f.readlines()
	# x = sorted(lines,key=sortLongest)
	results = []
	for line in lines:
		x = (line.split())
		if len(x) > 0:
			results.append(max(x))
	longest = results[0]
	
	# for some reason print(max(results)) isn't returning the max value in the results list but the below code works'
	for word in results:
		if len(word) > len(longest):
			longest = word
			
	print(longest)


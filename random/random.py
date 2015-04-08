#!/usr/bin/env
"""
Author: Mohiuddin Rana
Date: 2/27/2014
"""
import time
from collections import OrderedDict

def random(min, max):
	"""
	Seed: This take the system time which is very long number and then slice then digit from 4 to 9
	1103515245 + 12345: Is a special number to generate a well distributed random number 
	First it generates 5 random numbers which is well distributed. 
	Then removes the duplicates from the list but  keeps the original order 
	Finally, it take the last random number from the list and give it to the user
	""" 
	randomList = []
	for i in range (0,5):
		timeseed = str(time.clock())[4:9]
		seed =int ((int (timeseed)*1103515245 + 12345)/65536) 
		randomList.append(int((seed % (max+1-min)) + min))
	listwithoutDuplicates= list(OrderedDict.fromkeys(randomList))
	return listwithoutDuplicates[len (listwithoutDuplicates)-1]



"""
Example Use:
Generate random number between -5 to 25
>>> random(-5, 25)
"""

"""
Generating 10*10 matrix of random number in between -5 to 25 
"""
for i in range (0,10):
	l = []
	for j in range (0,10):
		l.append(random(-5, 25))
	print l

"""
Sample output from the 10*10 

[16, -2, 17, -4, 19, 6, 13, 3, 25, -1]
[-3, -1, 5, 25, 2, -2, 23, 3, 10, -5]
[22, 23, 11, 14, 21, -1, 22, 1, 24, 16]
[-1, 16, 25, 13, 9, -3, 20, -4, 16, -4]
[13, 19, -2, -5, 16, 25, 17, 9, 21, 16]
[10, 19, 18, 4, 2, -2, 7, 17, 21, 0]
[-3, -3, 22, 1, 11, 11, 24, 24, 5, 22]
[10, 1, -1, -5, 8, 18, -3, 7, 17, 10]
[16, 7, 23, 19, 14, 10, 4, 14, 9, 20]
[-3, 12, 7, 1, 11, 20, -1, 25, 11, 5]

"""
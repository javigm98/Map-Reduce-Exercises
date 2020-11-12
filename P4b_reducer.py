#!/usr/bin/python3

import sys
import math
import re

prev = 0
ids = []

# We follow the example explained in class for the inverted index 
# map-reduce pattern. For each range we group all the film ids 
# (films with the same range will appear together due to the previous 
# sort) and print the resulting list. 

for line in sys.stdin:
	line = re.sub( r'^\W+|\W+$', '', line )
	range, id = line.split(' ')
	if int(range) > prev:
		if(prev > 0):
			print("Range " + str(prev) + ": " + str(ids) + '\n')
		prev = int(range)
		ids = [id]
	if id != ids[-1]:
		ids.append(id)
print("Range " + str(prev) + ": " + str(ids) + '\n')



'''
# Same idea but without using lists
for line in sys.stdin:
	line = re.sub( r'^\W+|\W+$', '', line )
	range, id = line.split(' ')
	if int(range) > prev:
		prev = int(range)
		print(str(prev)+ ": ")
		print("\t" + id)
	else:
		print("\t" + id)
		
'''

# Javier Guzmán Muñoz
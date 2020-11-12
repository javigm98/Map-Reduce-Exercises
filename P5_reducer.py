#!/usr/bin/python3

import sys

count = 0
sum = 0
previous = None

# We calculate the average mass for each meteorite class.
# Equal classes will appear together due to the previous sort.

for line in sys.stdin:
	recclass, mass = line.split('\t')
	if(recclass != previous):
		if previous is not None:
			print(previous + '\t' + str(sum/count))
		previous = recclass
		sum = 0
		count = 0
	sum += float(mass)
	count += 1
	
print(previous + '\t' + str(sum/count))

# Javier Guzmán Muñoz
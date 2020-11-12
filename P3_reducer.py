#!/usr/bin/python3

import sys

count = 0 # Stores the number of values processed for a year 
sum = 0   # Stores the addition of all the values for a year
previous = None

# We calculate the average value for each year. Data corresponding to the
# same year will arrive together due to the previous sorting.

for line in sys.stdin:
	year, close = line.split('\t')
	if(year != previous):
		if previous is not None:
			print(previous + '\t' + str(sum/count))
		previous = year
		sum = 0
		count = 0
	sum += float(close)
	count += 1
	
print(previous + '\t' + str(sum/count))

# Javier Guzmán Muñoz

#!/usr/bin/python3

import sys

previous = None
sum = 0

# We count in 'sum' the appearances of each URL
# Equal URLs will appear together due to the previous 
# sorting.

for line in sys.stdin:
	key, value = line.split(' ')
	
	if key != previous:
		if previous is not None:
			print(previous + ' ' + str(sum))
		previous = key
		sum = 0
	sum += int(value)
	
print(previous + ' ' + str(sum))

# Javier Guzmán Muñoz
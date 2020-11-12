#!/usr/bin/python3

import sys

sum = 0
count = 0
previous = None

# We calculate the average rating for each film.
# Equal films will appear together due to the previous sort.

for line in sys.stdin:
	id,rating=line.split(' ')
	if id != previous:
		if previous is not None:
			print(previous + ' ' + str(sum/count))
		previous = id
		sum = 0
		count = 0
	sum += float(rating)
	count += 1
	
print(previous + ' ' + str(sum/count))

# Javier Guzmán Muñoz
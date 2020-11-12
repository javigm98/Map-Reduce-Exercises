#!/usr/bin/python3

import sys
import re
import math

# The map function assigns to each film its corresponding range, that is, 
# the ceiling of its average rating.

for line in sys.stdin:
	line = re.sub( r'^\W+|\W+$', '', line )
	id,rating = line.split(' ')
	
	# We consider the special case when the average rating is zero, because 
	# the ceiling function of 0 is 0 and its corresponding range is 1.
	
	if float(rating) == 0: 
		range = 1
	
	# For the rest of the cases, the corresponding range is the ceiling of 
	# its average rating.
	
	else:
		range =  math.ceil(float(rating))
	print(str(range) + " " + id)
	
# Javier Guzmán Muñoz
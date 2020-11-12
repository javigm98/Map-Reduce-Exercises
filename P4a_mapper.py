#!/usr/bin/python3

import sys

# We extract the data and print only the part that is relevant for the 
# problem in each line: the film id and the rating 

for line in sys.stdin:
	_,id,rating,_ = line.split(',')
	print(id + " " + rating)

# Javier Guzmán Muñoz
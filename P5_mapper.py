#!/usr/bin/python3

import sys
import re
import csv

# In the map function we extract and print the data that is relevant:
# the meteorite class and the mass of each observation.

# We use csv library to easily read the input and process the data.

for line in csv.reader(sys.stdin, delimiter=',', quotechar='"'):
	mass = line[4]
	recclass = line[3]
	
	# We clean the input and we throw out the lines that do not contain 
	# information for the mass or the meteorite class and those with a mass 
	# of 0, which obviously represent wrong data.
	
	# In this exercise we do not consider any other mistakes in the input, 
	# such as considering R3/4, R3-4, R3.4 as the same class because in fact 
	# this is something that we can't know for sure.
	
	# Also there are cases where the class is "H6" or "H6 " and we also 
	# consider them as different ones due to the difficulty of cleaning 
	# this data and the various options that could appear.
	
	if(mass != '' and recclass != ''):
		if float(mass) > 0:
			print(recclass + '\t' + mass)
			
# Javier Guzmán Muñoz
		
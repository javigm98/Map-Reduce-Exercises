#!/usr/bin/python3

import sys
import csv

# The map function only prints the year and the stock price at close 
# from each input line.

# We use csv library to easily extract the information from the input.

for line in csv.reader(sys.stdin, delimiter=','):

	# We extract the year from the date
	
	year = int(line[0][0:4])
	if(year >= 2009):
		print(str(year) + '\t' + line[4]) #line[4]: Close
		
# Javier Guzmán Muñoz
		
		
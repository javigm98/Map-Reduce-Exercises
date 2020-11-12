#!/usr/bin/python3

import sys
import re

for line in sys.stdin:
	
	line = re.sub( r'^\W+|\W+$', '', line )
	
	# The given word is compared with each one in the line from the input.
	# We check if the word is in the line without considering upper case
	# letters.
	
	for word in re.split(r"\W+", line):
		if word.lower() == sys.argv[1].lower():
		
			# When we find a coincidence, we print the line and end the 
			# processing of that line
			
			print (line)
			break;
			
# Javier Guzmán Muñoz
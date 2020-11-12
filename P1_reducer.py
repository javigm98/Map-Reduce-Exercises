#!/usr/bin/python3

import sys
import re

# The reduce function is the identity.

for line in sys.stdin:
	line = re.sub( r'^\W+|\W+$', '', line )
	print (line)
	
# Javier Guzmán Muñoz
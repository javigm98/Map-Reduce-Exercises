#!/usr/bin/python3

import sys
import re

for line in sys.stdin:

	# According to the structure of the input file, first we split by '"', focussing
	# on the second part of the split, where we have the command (GET, POST, OPTIONS)
	# and where URLs can appear. Next, we split by ' ', because if we have an URL the
	# structure would be "COMMAND URL PROTOCOL". So here, we first check that the
	# split has divided the line in three parts (the ones mentioned before) and then
	# we check if the second of these three parts matches with the RE of an URL (here
	# we consider an URL as a / followed by one or more characters that are not 
	# white spaces).
	
	_,inst,_ = line.split('\"')
	instr_sep = inst.split(" ")
	if len(instr_sep) == 3:
		dir = re.search(r"/\S+", instr_sep[1])
		if dir is not None:
			print(dir.group(0) + " 1")
			
# Javier Guzmán Muñoz
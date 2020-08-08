#! python3

import csv, sys, argparse, pyperclip  			# pyperclip is a third party library, and will need to be installed. I'd recommend using Pip to install it

parser = argparse.ArgumentParser(description='Takes in two file paths (-p is primary and -s is secondary), and subtracts the contents of one from the other')  # generate the argument parser

parser.add_argument('-p')  						# add the ability to use '-p' and '-s' flags at command line. Failure to pass the arguments, or non-csv files will fail with a type error at line 28
parser.add_argument('-s')

paths = parser.parse_args()						# parse the arguments to a list of strings

def csv_toList(filePath):
	with open(filePath) as primary_data_file:					# using a 'with' statement means we automatically close the file after execution
		reader = csv.reader(primary_data_file)
		lst = list(reader)										# returns a list of list objects
		flatList = [x for le in lst for x in le]  				# this converts the list of lists into a flat list
		stripList = [element.strip() for element in flatList]	# strips newlines, tabs etc. 
	return stripList

try:
	primary = csv_toList(paths.p)				# retruns the primary list
	secondary  = csv_toList(paths.s)			# returns the secondary list

	filteredList = [x for x in primary if x not in secondary]	# list comprehension. Removes any elements found in the first list from the second list
	print(f'Removed {len(primary)-len(filteredList)} items from primary list. Output is now on your clipboard')  # identifies how many items have been removed from the primary list
	pyperclip.copy('\n'.join(filteredList))		# copies the new list, with newline characters between each element, onto the clipboard

except TypeError:								#Only triggers if the type of the file passed is not a csv / no arguments passed
	print('You need to pass two file paths')
	exit()




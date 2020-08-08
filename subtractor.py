#! python3

import csv, sys, argparse, pyperclip

parser = argparse.ArgumentParser(description='Takes in two file paths (-p is primary and -s is secondary), and subtracts the contents of one from the other')

parser.add_argument('-p')
parser.add_argument('-s')

paths = parser.parse_args()

def csv_toList(filePath):
	with open(filePath) as primary_data_file:
		reader = csv.reader(primary_data_file)
		lst = list(reader)	#returns a list of list objects
		flatList = [x for le in lst for x in le]  #this converts the list of lists into a flat list
		stripList = [element.strip() for element in flatList]
	return stripList

try:
	primary = csv_toList(paths.p)
	secondary  = csv_toList(paths.s)

	filteredList = [x for x in primary if x not in secondary]
	print(f'Removed {len(primary)-len(filteredList)} items from primary list. Output is now on your clipboard')
	pyperclip.copy('\n'.join(filteredList))

except TypeError:
	print('You need to pass two file paths')
	exit()




import time
import datetime
import os  
import sys   
import argparse             


#pull and check args with argparse   

parser = argparse.ArgumentParser()
parser.add_argument('directory', action='store', help='Insert path to directory')
parser.add_argument('direction', action='store', help = 'Choose sorting order', choices=['ascending','descending'], 
default = 'ascending')
parser.add_argument('by', action='store', choices = ['size','mtime','filename'], default = 'filename')

parser.add_argument('top_n', action='store', type = int, help='Insert number of top results to be displayed')

argvals = parser.parse_args()

directory = argvals.directory
by = argvals.by
direction = argvals.direction
top_n = argvals.top_n


#populate dictionary with data

def pull_data(mydir):
	maindict = {}
	for item in os.listdir(mydir):
		fullpath = os.path.join(mydir,item)
		maindict[item] = {'name': os.path.basename(item),'size': os.path.getsize(fullpath),
		'mtime': os.path.getmtime(fullpath)}
	return maindict


dictionary = pull_data(directory)

#sort and select top requested files
def sorted_data(dictionary, by, top_n, direction):
	if direction == 'ascending':
		sorted_dict = sorted(dictionary, key = lambda x: dictionary[x][by])[:top_n]
	
	else:
		sorted_dict = sorted(dictionary, key = lambda x: dictionary[x][by], reverse=True)[:top_n]

	return sorted_dict

sorted_dictionary = sorted_data(dictionary, argvals.by, argvals.top_n, argvals.direction)


#print sorted files

for item in sorted_dictionary:
	print item   
	
	

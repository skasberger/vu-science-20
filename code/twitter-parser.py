#!/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

import json
import os
import csv

__author__ = "Stefan Kasberger"
__copyright__ = "Copyright 2015"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Stefan Kasberger"
__email__ = "mail@stefankasberger.at"
__status__ = "Prototype" # 'Development', 'Production' or 'Prototype'


###    GLOBAL   ###


ROOT_FOLDER = os.path.dirname(os.getcwd()) # sets root folder to one directory up
FILE_TWEETS_IN = ROOT_FOLDER + '/data/raw/csv/tweets.csv'
FILE_TWEETS_OUT = ROOT_FOLDER + '/data/csv/mentions.csv'


###    FUNCTIONS   ###

def Save2File(data, filename):
	"""Saves file on specified place on harddrive.
	
	Args:
		data: string to save
		filename: name of the file
	
	Returns:
		na
	"""
	text_file = open(filename, "w")
	text_file.write(data.decode('utf-8'))
	text_file.close()


def ReadText(filename):
	"""Reads file and returns the text.
	
	Args:
		filename: name of the file
	
	Returns:
		text: content of file as string
	"""
	f = open(filename, 'r')
	text = f.read()

	return text


###    MAIN   ###


if __name__ == "__main__":
	#data = ReadText(FILE_TWEETS_IN)
	#print data[:5]
	csvString = 'tweeter; mentioned\n'
	firstline = True
	with open(FILE_TWEETS_IN) as csvfile:
		csvfile.readline()
		mentionreader = csv.reader(csvfile, delimiter=';', quotechar='"')
		for row in mentionreader:
			entities_str = json.loads(row[17])
			for mention in entities_str['user_mentions']:
				csvString = csvString + row[1] + '; ' + mention['screen_name'] + '\n'
	Save2File(csvString, FILE_TWEETS_OUT)





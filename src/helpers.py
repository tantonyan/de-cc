# the helper functions and global variables

import string # using the string.punctuation constant
import bisect # using the bisect.insort - insert into a sorted list
import math # using floor for the median

wordCount = {} # global: a dictionary that will keep the ongoing word:count 
wordsPerLine = [] # global: sorted list - for each next line, we add the word count
runningMedian = [] # global: a list to keep the running medians


### cleanText: cleanup one line of text (any string) and convert to lowercase
def cleanText(line):
	cleanLine = line.translate(None, string.punctuation)	# clean the unwanted characters
	return cleanLine.lower()				# convert to lowercase


### addWordsWC: add the list of words to our dictionary of word:count
def addWordsWC(words):
	global wordCount # use the global var to build up the counts
	# loop through the list and process one at a time
	for word in words:
		if wordCount.has_key(word): # already encountered this word, just +1 the count
			wordCount[word] += 1 
		else:
			wordCount[word] = 1


### addWordsRM: process the next line for the running median 
def addWordsRM(words):
	global wordsPerLine
	global runningMedian
	
	numOfWords = len(words) # number of words is all we need for this process
	
	bisect.insort(wordsPerLine, numOfWords) # sorted insert
	
	# find the middle element or mean of the middle two elements
	lines = len(wordsPerLine) # number of lines (including the current line) - list size
	middleIndex = int(math.floor(lines/2)) # middle or the right one

	median = wordsPerLine[middleIndex]  
	median *= 1.0 # to force a float type
	
	if lines & 1 == 0: # if an even number
		median = (median + wordsPerLine[middleIndex - 1]) / 2

	runningMedian.append(median) # add to the global list


### runForFile: run both processes (word count and running median) on one file
###		read each line, clean from punctuations and store as list of words
###		1. use the list of words for the word count process
###		2. use the list of words for the running median process
def runForFile(filePath):
	try:
		inFile = open(filePath, "r")
	except: # IO, Permission, etc.
		print "Error while opening " + filePath + " skipping..."
		return

	# read only one line at a time as the file might be large
	for nextLine in inFile: 
		cleanLine = cleanText(nextLine)

		words = cleanLine.split() # get list of words

		addWordsWC(words) # process the list for word count problem
		addWordsRM(words) # process the list for running median

	inFile.close()


### writeWordCount: write word \t count to a file from the dictionary
def writeWordCount(filePath):
	try: # first try to open the file
		outFile = open(filePath, "w")
	except: # IO, Permission, etc.
		print "Error while opening " + filePath
		return
	
	global wordCount # read from the global var
	
	# take the keys list and sort it - can't sort the dictionary
	words = wordCount.keys()
	words.sort() # sort in-place

	# iterate and write
	for word in words:
		outFile.write(word + "\t" + str(wordCount[word]) + "\n")

	outFile.close()


### writeRunningMedian: write the generated list of the running medians
def writeRunningMedian(filePath):
	try: # first try to open the file
		outFile = open(filePath, "w")
	except: # IO, Permission, etc.
		print "Error while opening " + filePath
		return

	global runningMedian # write the generated list one number per line

	# loop through and write
	for median in runningMedian:
		outFile.write(str(median) + "\n")

	outFile.close()


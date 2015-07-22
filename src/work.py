# do the high level work here

import os
import os.path

# our modules
import constants
import helpers

# loop through the input directory and process each file
allItems = os.listdir(constants.inputDir)
allItems.sort() # we need the list in alphabetical order for the running median
for nextItem in allItems:
	item = constants.inputDir + nextItem # get the path to it

	if not os.path.isdir(item): # only interested in files
		print "Found an input file: " + item
		helpers.runForFile(item) # run word count

# finally, write the outputs
helpers.writeWordCount(constants.wcOutputFile)
helpers.writeRunningMedian(constants.medOutputFile)

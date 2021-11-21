# carl hentges NOV 2021
# This script checks all the files in the similarity of all the images
# in the fileDB folder to a image given as part of the CMD, and then returns
# the image with the smallest (most similar) value.
#
# HOW IT WORKS:
# The image_match library generates a 'finger print' for each image and then
# finds the normalized distance between signatures which constitutes a similarity
# score. See http://www.cs.cmu.edu/~hcwong/Pdfs/icip02.ps for more info.
#
# HOW TO RUN:
# 1) Ensure that the constant variables such as DB_DIR TEST_IMG_DIR and
# MIN_SIM_LOW_LIM are set to the correct values.
# 2) Then execute:
# >>> python3 testSimilarity.py <test_image>
# 3) Where <test_image> is the name of the image you want to test for
# the program will then go through all the images in the testDB and will
# give a similarity score for each one, with the one with the lowest (most
# similar) image being returned, then if that similarity is less than the set
# limit it will return FALSE, indicating that the image is too similar to an
# exiting image to be used.
#

from image_match.goldberg import ImageSignature
import os
import sys


DB_DIR='./fileDB/' # path to database directory
TEST_IMG_DIR ='./' # path to test image directory
MIN_SIM_LOW_LIM = 0.3 # the limit for matching images similarity score
fileDB = os.listdir(DB_DIR)
minSim = 1.00 # the current minimum similarity
minSimMatch = '' # the file with the minSim


#make sure that you have a image to test
assert(len(sys.argv) == 2), "Must take CMD ONE argument for test image!"
testImage = sys.argv[1] # the 1st argument is the image name

print("test image:",testImage)

# init. generator object and make signature of the test image
gis = ImageSignature()
testImageSigniture = gis.generate_signature(TEST_IMG_DIR+testImage)


for image in fileDB :
	# if the DB contains "hidden" files don't check them and just move on 
	if image[0] == '.':
		continue

	print("current comparison image:",image)

	# generate a signature of the current comparison file
	tempImageSigniture = gis.generate_signature(DB_DIR+image)
	currentSim = gis.normalized_distance(tempImageSigniture,testImageSigniture)

	# update the the current most similar image
	if currentSim < minSim:
		minSim = currentSim
		minSimMatch = image

# the most similar image score and image
print("lowest similarity:",minSim,minSimMatch)

# this is the final output TRUE if the image is novel enough to upload and
# FALSE if the image is too similar to an exiting image
print(minSim>=MIN_SIM_LOW_LIM)






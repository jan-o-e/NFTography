# carl hentges NOV 2021
# this script checks all the files in the similarity of all the images
# in the fileDB folder to a image given as part of the CMD, and then returns
# the image with the smallest (most similar) value 
from image_match.goldberg import ImageSignature
import os
import sys
gis = ImageSignature()


DIR="/Users/carl/NFTography/fileDB/"
MIN_SIM_LIM = 0.3 # the limit for matching images similarity score

#make sure that you have a image to test
assert(len(sys.argv) == 2), "Must take CMD ONE argument for test image!"
testImage = sys.argv[1]

print("test image:",testImage)

fileDB = os.listdir(DIR)
minSim = 1.00 # the current minimum similarity
minSimMatch = testImage # the file with the minSim
testImageSigniture = gis.generate_signature(testImage)
for image in fileDB :
	if image == '.DS_Store':
		continue
	print("current comparison image:",image)
	tempImageSigniture = gis.generate_signature(DIR+image)
	currentSim = gis.normalized_distance(tempImageSigniture,testImageSigniture)
	if currentSim < minSim:
		minSim = currentSim
		minSimMatch = image
print("lowest similarity:",minSim,minSimMatch)
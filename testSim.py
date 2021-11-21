from image_match.goldberg import ImageSignature
import os
import sys

DIR="/Users/carl/NFTography/fileDB/"

gis = ImageSignature()
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

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
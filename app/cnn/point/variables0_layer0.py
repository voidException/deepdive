#! /usr/bin/env python
#Author: Amir S 

from helper.easierlife import *
import json
import fileinput

BASE_FOLDER = "/Users/Amir/Desktop/Spring2014/DeepDive/app/cnn"

FID_IN=1
for row in fileinput.input():
	obj = json.loads(row)
	image_id = obj["image_id"]
	pixels= deserialize(obj["pixels"])

	num_rows, height, depth = pixels.shape
	for i in range(0, num_rows):
		for j in range(0, height):
			for k in range(0,depth):
				color = float(pixels[i][j][k])
			color=color/3
			f=0
			print json.dumps({
				"vector_id": str(image_id)+","+str(i*height+j),
				"image_id":image_id,
				"x":i,
				"y":j,
				"value":color,
				"fid":f
				})
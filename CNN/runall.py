from scipy.io import loadmat
import os

num_of_nn = 5000

mapping = {}
with open("train.txt") as f:
	for line in f:
		line = line.rstrip().split(' ')
		if line[0].split('/')[0] not in mapping:
			mapping[line[0].split('/')[0]] = line[1]

obj = loadmat("D:/NUS/Course/1516sem1/CS5228/newresult")
#1 Genearate train.txt val.txt
for i in range(len(obj["query_image_path"])):
	line = obj["query_image_path"][i].split("\\")
	if line[0] in mapping:
		with open("val200.txt", "wb") as f:
			f.write(line[0] + "/" + line[1].strip() + " " + mapping[line[0]] + "\r\n")
			f.close()
		with open("train200.txt", "wb") as f:
			for j in range(num_of_nn):
				train_item_index = obj["result"][i][j]
				temp = obj["train_image_path"][train_item_index].split("\\")
				f.write(temp[0] + "/" + temp[1].strip() + " " + mapping[temp[0]] + "\r\n")
			f.close()
		with open("run_train_imagenet.bat", "wb") as f:
			f.write("@echo off\r\ncall train_imagenet.bat >" + str(i) + ".txt 2>&1")
			f.close()
		with open("autorun.bat", "rb") as f:
			for command in f:
				command = command.strip()
				os.system(command)
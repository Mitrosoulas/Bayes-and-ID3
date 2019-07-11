#Stathopoulow Dhmhtrios(3150165)
#Vlachos Christos(3150014)

import math
import copy
import ID3Reader
import MethodMan

from ID3 import ID3

def run():
	print("Executing ID3 algorithm")
	examples = ID3Reader.Read()


	DTree = ID3(examples,"ghost","ghost",0)
	j = 0


	accuracy = 0

	print("#######################################")
	newExamples = open("./ID3/readyData.txt",'r')
	for line in newExamples:
		j+=1
		ex = line.split(',')
		for i in range(len(ex)):
			ex[i] = ex[i].rstrip()
		tempEx = []
		for i in range(0,len(ex) -1):
			tempEx.append(ex[i])
		answer = DTree.answer(tempEx)
		if answer == ex[4]:
			accuracy += 1
		print("Test subject "+str(j))
		print("Algorithm category of choice is : "+answer)
		print("Actual category is : "+ex[-1] )
		print("#######################################")

	return str("ID3 algorithm accuracy with "+ str(len(examples))+" examples of Iris flowers is: "+str(accuracy)+"/30")

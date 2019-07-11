#Stathopoulow Dhmhtrios(3150165)
#Vlachos Christos(3150014)

import BReader 
import methodMan

def ReadIn():
	file = open ("./Bayes/newData.txt",'r')
	#Read from file
	examples = []
	array = []
	for line in file :
		if(  line.strip()):
			examples.append(line)
			


	for i in examples :
		array.append(i[::-1])


	array.sort()

	for i in range (len(array)) :
		examples[i] = array[i][::-1]
	file.close()
	return examples

	
	

def run():

	print("Executing Naive Bayes algorithm")
	convert = methodMan.convert
	bayes = BReader.bayes

	
	
	
	#Transforming Dataset
	
	file = open ("./Bayes/data.txt",'r')
	newFile = open("./Bayes/newData.txt",'w')
	examples = open("./Bayes/testData.txt",'r')
	newExamples = open("./Bayes/readyData.txt",'w')
	
	try:
		convert(file,newFile)
		newFile.close()
		convert(examples,newExamples)
	except:
		print()

	
	#USED IN BAYES ALGORITHM	

	examplesArr = ReadIn()
	accuracy = 0
	types = [4,6,4,5]
	newExamples.close()
	newExamples = open("./Bayes/readyData.txt",'r')
	j = 0
	for line in newExamples:
		j +=1
		ex = line.split(',')
		for i in range(len(ex)):
			ex[i] = ex[i].rstrip()
		tempEx = []
		for i in range(0,len(ex) -1):
			tempEx.append(ex[i])
		answer = bayes(tempEx,types,ReadIn())
		if answer == ex[4]:
			accuracy += 1
		
		print("Test subject "+str(j))
		print("Algorithm category of choice is : "+answer)
		print("Actual category is : "+ex[-1] )
		print("#######################################")
	error = 1 - (accuracy/30)
	return str("Accuracy of Naive Bayes algorithm with " +str(len(examplesArr))+" examples of Iris flowers is: "+str(accuracy)+"/30")








#Stathopoulow Dhmhtrios(3150165)
#Vlachos Christos(3150014)

def attr(n,type):
	if type == 0:
		
		if n in range(43,53) : return "A1A"
		if n in range(53,61) : return "A1B"
		if n in range(61,67) : return "A1C"
		if n in range(67,80) : return "A1D"
	if type == 1:
		
		if n in range(20,28) : return "A2A"
		if n in range(28,30) : return "A2B"
		if n in range(30,31) : return "A2C"
		if n in range(31,33) : return "A2D"
		if n in range(33,36) : return "A2E"
		if n in range(36,45) : return "A2F"
	if type == 2:
		
		if n in range(10,16) : return "B1A"
		if n in range(16,46) : return "B1B"
		if n in range(46,56) : return "B1C"
		if n in range(56,70) : return "B1D"
	if type == 3:
		
		if n in range(1,3) : return "B2A"
		if n in range(3,13) : return "B2B"
		if n in range(13,16) : return "B2C"
		if n in range(16,21) : return "B2D"
		if n in range(21,26) : return "B2E"
	

#CREATING A NEW DATASET WITH DISTINCT VALUES AS DESCRIBED IN PDF

def convert(file,newFile):
	for line in file:
	
		words = line.split(",")
	
	
		words[0] = attr(int(10*float(words[0])),0)
		words[1] = attr(int(10*float(words[1])),1)
		words[2] = attr(int(10*float(words[2])),2)
		words[3] = attr(int(10*float(words[3])),3)
		if None not in words:
			newFile.write(words[0])
			newFile.write(",")
			newFile.write(words[1])
			newFile.write(",")
			newFile.write(words[2])
			newFile.write(",")
			newFile.write(words[3])
			newFile.write(",")
			newFile.write(words[4])
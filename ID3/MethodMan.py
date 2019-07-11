#Stathopoulow Dhmhtrios(3150165)
#Vlachos Christos(3150014)
import math
import copy

def sameCat(examples):
	
	tempCategory = set(Attributes(examples,-1))
	if len(tempCategory) == 1:
		return next(iter(tempCategory))
	return "False"



import math

def TypeCount(category,Sp):
	count = 0
	num = []
	for i in Sp:
		for j in  category :
			if(i == j ):
				count+=1
		num.append(count)
		count = 0
	return num

def Attributes(examples,j) :
	category = []
	for i in range(len(examples)):
		category.append(examples[i][j])
	return category

def Entropy(Att,Sp,AttNum,Category,SpCat):
	array = []
	sum = 0

	for i in range(len(Sp)):
		H = 0
		for j in SpCat:
			count = 0
			for k in range (len(Category)):
				if(Att[k] == Sp[i] and Category[k] == j ):

					count+=1
			if(count != 0):
				H += (count / int(AttNum[i])) * math.log2(count / int(AttNum[i]))

		array.append(-H * AttNum[i]/len(Category))
	for i in array :
		sum+=i
	return sum


def Distinct(list):
	SetArr = set(list)
	Cat = []
	for i in SetArr:
		Cat.append(i)
	return Cat

def chooseExamples(examples,value,index):
	IExamples = []
	
	for y in range(len(examples)):
		if examples[y][index] == value:
			temp = copy.deepcopy(examples[y])
			
			IExamples.append(temp)
			
	
	return IExamples
	
#############################################################################
def InfoGain(examples, Hc,catnum,category,SpCat):
    IG = []
    entropy = 0

    for j in range ( len(examples[0])-1):
        att = Attributes(examples, j)
        
        Sp = Distinct(att)
        
        catnum = TypeCount(att,Sp)
        
        entropy = Hc - Entropy(att,Sp,catnum,category,SpCat)
        IG.append(entropy)
    

    max = IG[0]
    pos = 0
    for i in range (len(IG)) :
        if(IG[i] > max):
            max = IG[i]
            pos = i
    return pos
#################################################

def CHOOSEATTRIBUTE(examples):
	category = Attributes(examples,-1)
	total = len(category)



	SpCat = Distinct(category)


	
	CAtNum = TypeCount(category,SpCat)
	


	Hc = 0
	for i in CAtNum :
		Hc += (i/total) * math.log2(i/total)
	Hc = -Hc


	return  InfoGain(examples, Hc,CAtNum,category,SpCat)
	
def MAJORITYVALUE(examples):
	
	L = Attributes(examples,-1)
	sP = Distinct(L)
	
	num = TypeCount(L,sP)
	index = 0
	max = 0
	for x in range(len(num)):
		if num[x]>max:
			index = x
			max = num[x]
	
	return sP[index]

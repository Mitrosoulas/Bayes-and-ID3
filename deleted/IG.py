import math
import Reader
import MethodMan
M = MethodMan

def InfoGain(examples, Hc,catnum,category,SpCat):
    IG = []
    entropy = 0

    for j in range ( len(examples[0])-1):
        att = M.Attributes(examples, j)
        Sp = M.Discrete(att)
        #print(Sp)
        catnum = M.TypeCount(att,Sp)
        #print(catnum)

        entropy = Hc - M.Entropy(att,Sp,catnum,category,SpCat)
        IG.append(entropy)
       # print ( "Information gain for Attribute "+ str(j) + " is :" )
        #print(entropy)

    max = IG[0]
    pos = 0
    for i in range (len(IG)) :
        if(IG[i] > max):
            max = IG[i]
            pos = i
    return pos
#################################################
#examples = Reader.Read()
def CHOOSEATTRIBUTE(examples)
	category = M.Attributes(examples,-1)
	total = len(category)



	SpCat = M.Discrete(category)


	#print(SpCat)
	CAtNum = M.TypeCount(category,SpCat)
	#print(CAtNum)


	Hc = 0
	for i in CAtNum :
		Hc += (i/total) * math.log2(i/total)
	Hc = -Hc


	return = InfoGain(examples, Hc,CAtNum,category,SpCat)
	#print ("Attribute with greates IG = " + str(index))




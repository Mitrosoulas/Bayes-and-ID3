#Stathopoulow Dhmhtrios(3150165)
#Vlachos Christos(3150014)

import copy
from DTree import DTree
from MethodMan import *

def ID3(examples1,default,givenValue,givenIndex):
	
	examples = copy.deepcopy(examples1)
	category = default
	if len(examples) == 0:
		return DTree(default,givenValue,givenIndex)
	elif sameCat(examples) != "False":
		return DTree(sameCat(examples),givenValue,givenIndex)
	elif len(examples) == 1:
		return DTree(default,givenValue,givenIndex)
	else:
		index = CHOOSEATTRIBUTE(examples)
		best = Distinct(Attributes(examples,index))
		m = MAJORITYVALUE(examples)
		tree = DTree(m,givenValue,index)
		for value in best:
			
			IExamples = chooseExamples(examples,value,index)
			subTree = ID3(IExamples,m,value,index)
			tree.add(subTree)
		
		
		return tree
		

#Stathopoulow Dhmhtrios(3150165)
#Vlachos Christos(3150014)

import copy

class DTree:

	
	def __init__(self,majorityCategory,value="__other__",attributeIndex=0):
		self.children = []
		self.value = value
		self.attributeIndex = attributeIndex
		self.majorityCategory = majorityCategory
		
	
	def add(self,subTree):
		self.children.append(subTree)
		
	def isLeaf(self):
		if len(self.children) == 0:
			return True
		return False
		
	def __str__ (self):
		if self.isLeaf():
			return "\n" + self.majorityCategory
		else:
			for x in self.children:
				print(x)
				return "\n" + self.majorityCategory

	def print(self):

		print(self.value)
		for x in self.children:
			x.print()
		

	def answer(self,ex):
		cat = self.majorityCategory
		if self.isLeaf():
			return cat
		for x in self.children:
			if ex[self.attributeIndex] == x.value:
				return x.answer(ex)
		else:
			return cat
		
class id:
	def __init__(self,c):
		self.c = c
		self.exists = True
	



class Arr:
	def __init__(self,size):
		self.array = []
		for i in range(size):
			self.array.append(id(0))
		
	def __getitem__(self,i):
		temp = None
		count = 0
		for x in range(len(self.array)):
			if self.array[x].exists:
				if count == i:
					self.array[x].exists = False
					return self.array[x]
				else:
					count += 1
		return None


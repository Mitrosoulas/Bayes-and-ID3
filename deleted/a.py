import copy

def chooseExamples(examples,value,index):
	IExamples = [[None for x in range(len(examples))] for y in range(len(examples[index]))]
	temp = [[None for x in range(len(examples))] for y in range(len(examples[index]))]
	for y in range(len(examples[index])):
		if examples[y][index] == value:
			temp[y] = examples[y]
			temp[y].pop(index)
			
	for x in range(len(temp)):
		IExamples[x] = temp[x]
	return IExamples
	
	
	
	
	
	
examples = []
count = 0
for x in range(4):
	examples.append([])
	for y in range(4):
		count += 1
		examples[x].append(count)

newList = chooseExamples(examples,6,1)
print(newList)
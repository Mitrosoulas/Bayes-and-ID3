#Stathopoulow Dhmhtrios(3150165)
#Vlachos Christos(3150014)
def Read():
    file = open("./ID3/data.txt", 'r')
    examples = []
    temp = ""
    total = 0
    array = []

    categories = []

    # Read from file
    for line in file:
        if (line.strip()):
            examples.append(line)
            total += 1

    for i in examples:
        array.append(i[::-1])

    array.sort()

    for i in range(len(array)):
        examples[i] = array[i][::-1]

    # Create the example and attribute array
    for i in range(len(examples)):
        examples[i] = examples[i]  # [:-2]
        examples[i] = examples[i].split(",")

    for i in range(len(examples)):
        for j in range(len(examples[i])):
            examples[i][j] = examples[i][j].strip()
    file.close()
    return examples









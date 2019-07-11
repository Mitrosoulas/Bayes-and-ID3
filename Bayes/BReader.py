#Stathopoulow Dhmhtrios(3150165)
#Vlachos Christos(3150014)

import math

def bayes (insert,types,examples):

    
    
    category = []
    catnum = []
    count = 0
    temp = ""
    array = []
    categories = []




    #Create the example and attribute array
    for i in range (len(examples)):
        examples[i] = examples[i]#[:-2]
        examples[i] = examples[i].split(",")

    for i in range (len(examples)):
        for j in range (len(examples[i])):
            examples[i][j] = examples[i][j].strip()

    #Find category
    for i in range(len(examples)) :
        category.append(examples[i][-1])



    #Count each category
    temp = category[0]
    for i in category :
        if( i != temp ):
            temp = i
            catnum.append(count)
            count = 1
        else :
            count+=1
    catnum.append(count)

    categories.append(examples[0][-1])
    count = catnum[0]
    for i in range (1,len(catnum)-1):
        categories.append(examples[count][-1])
        count += catnum[i]

    categories.append(examples[count][-1])

    ######################BAYES#############################
    depth = 0
    sum = 0
    posibilities = []

    for i in range(len(catnum)):
        pos = catnum[i]/len(examples)
        for k in range(len(examples[0]) - 1):
            for j in range (catnum[i]):
                if(examples[j + depth][k] == insert [k]):
                    sum+=1
           
            pos*=(sum+1)/(catnum[i] + int(types[k]))
            sum = 0
        
        posibilities.append(pos)
        depth += catnum[i]



    
    max = 0


    for i in range(len(posibilities)):
        if (posibilities[max]<posibilities[i]):
            max = i


    return categories[max]



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


def Discrete(list):
    SetArr = set(list)
    Cat = []
    for i in SetArr:
        Cat.append(i)
    return Cat
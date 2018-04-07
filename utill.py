import bisect
runnin_index = 0

#[solcubuk,sagcubuk,solkatsayi,sagkatsayi,index_rec, running_index, isAvail,   formüllü_sey]

epsilon = 0.00001
concats_actions = []

def setRunIndex(n):
        global runnin_index
        runnin_index=n

def getStressByEnzim(enzim1, enzim2):
        pass

def getStressByIndex(liste, i1, i2):
        pass


def getLeftSorteds(liste):
        m = list(map(lambda x: x+[x[0]*x[1]/(x[3]+epsilon)], liste))
        return sorted(m, key=lambda x: x[7])

def getRightSorteds(liste):
        m = list(map(lambda x: x+[x[1]/(x[2]+epsilon)] , liste))
        return sorted(m, key=lambda x: x[7])

def getLeftComp(leftComp, rightComp): #FOR NOW
        for i in leftComp:
                if(i[6]==False):
                        continue

                for j in rightComp:
                	if(j[5] == i[5]):
                		j[6] = False
                		break
                
                return i
                

        return None

def getRightComp(rightComp,cubuk_sayi):
        for i in rightComp:
                if(i[6]==False):
                        continue
                return i

        return None


def concat(ele1, ele2):

    return ele1 + ele2


def generateNewComp(leftComp,rightComp, leftCSort, rightCSort):
    
    global concats_actions
    global runnin_index

    solc = leftComp[0]
    sagc = rightComp[1]
    solkat = leftComp[2]
    sagkat = rightComp[3]
    index = concat(leftComp[4], rightComp[4])
    
    concats_actions.append([index[0], index[-1]])

    for i in leftCSort:
        if( i[5] == leftComp[5] ):
            i[6] = False
            break

    for i in rightCSort:
        if( i[5] == rightComp[5] ):
            i[6] = False
            break

    new_enzim = [solc,sagc,solkat,sagkat,index,runnin_index,True]
    runnin_index += 1
    time = solc*leftComp[1]*sagc
    return (new_enzim,time)

    #[solcubuk,sagcubuk,solkatsayi,sagkatsayi,index, isAvail, formül]

def addComp(newComp,leftComp,rightComp):
        newCompRight = newComp + [newComp[1]/(newComp[2]+epsilon)]
        newCompLeft = newComp + [[newComp[0]*newComp[1]/(newComp[3]+epsilon)]]
        bisect.insort(leftComp,newCompLeft)
        bisect.insort(rightComp,newCompRight)
        

def getFinalIndex(leftComp):
        
        for i in leftComp:
                if(i[6]==True):
                        return i[4]

        print("THIS SHOULD NOT HAPPEN")

def getActionArray():
        global concats_actions
        return concats_actions

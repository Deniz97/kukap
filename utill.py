import bisect
runnin_index = 0

#[solcubuk,sagcubuk,solkatsayi,sagkatsayi,index_rec, running_index, isAvail,   formüllü_sey]

epsilon = 0.00001
concats_actions = []

def setRunIndex(n):
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
                i[6]=False
                for j in rightComp:
                        if( j[5] == i[5] ):
                                j[6] = False
                                break
                return i
                

        return None

def getRightComp(rightComp,cubuk_sayi):
        for i in rightComp:
                if(i[6]==False):
                        continue

                if( i[0] == cubuk_sayi):
                        i[6] = False
                        return i

        return None


def concat(ele1, ele2):

    if type(ele1) is int:
        ele1 = [ele1]
    if type(ele2) is int:
        ele2 = [ele2]

    return ele1 + ele2


def generateNewComp(leftComp,rightComp):

    global concats_actions

    solc = leftComp[0]
    sagc = rightComp[1]
    solkat = leftComp[2]
    sagkat = rightComp[3]
    index = concat(leftComp[4], rightComp[4])

    concats_actions.append([index[0], index[-1]])

    new_enzim = [solc,sagc,solkat,sagkat,runnin_index,True]
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
                if(leftComp[6]==True):
                        return i[4]

        print("THIS SHOULD NOT HAPPEN")

def getActionArray():
        global concats_actions
        return concats_actions

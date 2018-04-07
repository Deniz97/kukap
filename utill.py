import bisect
runnin_index = 0
#[solcubuk,sagcubuk,solkatsayi,sagkatsayi,index, isAvail, formüllü_sey]

def setRunIndex(n):
	runnin_index=n

def getStressByEnzim(enzim1, enzim2):
	pass

def getStressByIndex(liste, i1, i2):
	pass


def getLeftSorteds(liste):
	m = map(lambda x: x+[x[0]*x[1]/x[4]], liste)
	return sorted(lambda x: x[6] , m  )

def getRightSorteds():
	m = map(lambda x: x+[x[1]/x[3]] , liste)
	return sorted(lambda x: x[6] , m  )

def getLeftComp(leftComp): #FOR NOW
	for i in leftComp:
		if(i[5]==False):
			continue
		i[5]=False
		for j in rightComp:
			if( j[5] == i[5] ):
				j[5] = False
				break
		return i
		

	return None

def getRightComp(rightComp,cubuk_sayi):
	for i in rightComp:
		if(i[5]==False):
			continue

		if( i[0] == cubuk_sayi):
			i[5] = False
			return i

	return None

def generateNewComp(leftComp,rightComp):
	solc = leftComp[0]
	sagc = rightComp[1]
	solkat = leftComp[2]
	sagkat = rightComp[3]
	index = runnin_index
	runnin_index+=1
	
	new_enzim = [solc,sagc,solkat,sagkat,runnin_index,True]
	time =solc*leftComp[1]*sagc
	return (new_enzim,time)

	#[solcubuk,sagcubuk,solkatsayi,sagkatsayi,index, isAvail, formül]



def addComp(newComp,leftComp,rightComp):
	newCompRight = newComp + [newComp[1]/newComp[3]]
	newCompLeft = newComp + [[x[0]*x[1]/x[4]]]
	bisect.insort(leftComp,newCompLeft)
	bisect.insort(rightComp,newCompRight)
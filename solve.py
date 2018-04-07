from utill import *

n = int(input())
lst = [0] * n
result = [None] * n

ctr = 0
seqStr = ""

# lstElement ->
#   [solNoktaSayisi, sagNoktaSayisi, solKatsayi, sagKatsayi, index, isAvail]

if __name__ == '__main__':

    for i in range(n):
        lst[i] = [int(x) for x in input().split()] + [i, i, True] # TODO

   
    leftCompSorted = getLeftSorteds(lst)
    rightCompSorted = getRightSorteds(lst)

    setRunIndex(n)

    for _ in range(n-1):

        leftComp = getLeftComp(leftCompSorted, rightCompSorted)
        print(leftCompSorted)
        print()
        print()
        rightComp = getRightComp(rightCompSorted, leftComp[1])

        if rightComp is not None:

            newComp, comptime = generateNewComp(
                    leftComp, rightComp, leftCompSorted, rightCompSorted)

            addComp(newComp, leftCompSorted, rightCompSorted)

            ctr += comptime

    # finished all concatenations

    finalIndex = getFinalIndex(leftCompSorted)

    print(' '.join(map(lambda x: str(x), finalIndex)))
    print(ctr)

    actionArr = getActionArray()

    outputIndexes = [0] * n

    for i, num in enumerate(finalIndex):
        outputIndexes[num] = i

    for x, y in actionArr:
        print(outputIndexes[x], outputIndexes[y])



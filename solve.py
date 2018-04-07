n = int(input())
lst = [0] * n
result = [None] * n

ctr = 0

# lstElement ->
#   [solNoktaSayisi, sagNoktaSayisi, solKatsayi, sagKatsayi, index, isAvail]

if __name__ == '__main__':

    for i in range(n):
        lst[i] = [int(x) for x in input().split()] + [i, True] # TODO

   
    leftCompSorted = getLeftSorteds(lst)
    rightCompSorted = getRightSorteds(lst)

    setRunIndex(n)

    for _ in range(n-1):

        leftComp = getLeftComp(leftCompSorted, rightCompSorted)

        rightComp = getRightComp(rightCompSorted, leftComp[1])

        if rightComp is not None:

            newComp, comptime = generateNewComp(leftComp, rightComp)

            addComp(newComp, leftCompSorted, rightCompSorted)

            ctr += comptime

    # finished all concatenations
    
